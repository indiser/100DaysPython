"""
FREE MULTI-PROVIDER LLM ROUTER
Fails over automatically when quota or rate limits hit.

Providers used:
- Groq
- Cerebras
- Gemini
- HuggingFace

Usage:
from llm_router import chat_fast, chat_strong
"""

import os
import time
from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI
from google import genai
from huggingface_hub import InferenceClient

load_dotenv()

# =========================
# API KEYS (ENV VARIABLES)
# =========================
GROQ_KEY = os.getenv("GROQ_API_KEY")
CEREBRAS_KEY = os.getenv("CEREBRAS_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
HF_KEY = os.getenv("HUGGING_FACE_API_KEY")
OPENROUTER_KEY= os.environ.get("OPENROUTER_API_KEY")

# =========================
# CLIENT INITIALIZATION
# =========================
groq_client = Groq(api_key=GROQ_KEY) if GROQ_KEY else None
cerebras_client = OpenAI(
    api_key=CEREBRAS_KEY,
    base_url="https://api.cerebras.ai/v1"
) if CEREBRAS_KEY else None

gemini_client = genai.Client(api_key=GEMINI_KEY) if GEMINI_KEY else None

hf_client = InferenceClient(token=HF_KEY) if HF_KEY else None

openrouter_client = OpenAI(
    api_key=OPENROUTER_KEY,
    base_url="https://openrouter.ai/api/v1"
) if OPENROUTER_KEY else None


# =========================
# ERROR DETECTION
# =========================
def is_quota_error(e: Exception) -> bool:
    txt = str(e).lower()
    keywords = [
        "429", "quota", "rate", "capacity", "limit",
        "exceeded", "too many", "overloaded", "busy","400"
    ]
    return any(k in txt for k in keywords)


# =========================
# PROVIDERS
# =========================
def groq_chat(msgs):
    if not groq_client:
        raise RuntimeError("Groq key missing")
    r = groq_client.chat.completions.create(
        # model="llama-3.3-70b-versatile",
        model="openai/gpt-oss-120b",
        messages=msgs
    )
    return r.choices[0].message.content


def cerebras_chat(msgs):
    if not cerebras_client:
        raise RuntimeError("Cerebras key missing")
    r = cerebras_client.chat.completions.create(
        model="llama-3.3-70b",
        messages=msgs
    )
    return r.choices[0].message.content


def gemini_chat(msgs):
    if not gemini_client:
        raise RuntimeError("Gemini key missing")

    text = "\n".join(m["content"] for m in msgs)

    r = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )
    return r.text


def hf_chat(msgs):
    if not hf_client:
        raise RuntimeError("HF key missing")

    r = hf_client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=msgs
    )
    return r.choices[0].message.content

def openrouter_chat(msgs):
    if not openrouter_client:
        raise RuntimeError("OpenRouter key missing")
    
    # OpenRouter requires a specialized header for free tier routing
    r = openrouter_client.chat.completions.create(
        model="openrouter/free", 
        messages=msgs,
        extra_headers={
            "HTTP-Referer": "https://github.com/indiser/ViralContentFactory", # Optional but recommended by OpenRouter
            "X-Title": "ViralContentFactory" # Optional but recommended
        }
    )
    return r.choices[0].message.content
# =========================
# PROVIDER GROUPS
# =========================
CHEAP_PROVIDERS = [openrouter_chat, hf_chat, gemini_chat]        # classification, tagging
STRONG_PROVIDERS = [groq_chat, cerebras_chat]   # rewriting, reasoning
ALL_PROVIDERS = STRONG_PROVIDERS + CHEAP_PROVIDERS


# =========================
# CORE ROUTER
# =========================
def _ask_with_fallback(msgs, providers):
    last_error = None

    for provider in providers:
        try:
            return provider(msgs)

        except Exception as e:
            last_error = e
            print(f"[router] {provider.__name__} failed:", e)

            # quota or rate → try next provider
            if is_quota_error(e):
                print("[router] quota hit → switching")
                continue

            # transient error → retry once
            time.sleep(1)
            try:
                return provider(msgs)
            except Exception:
                continue

    raise RuntimeError(f"All providers failed: {last_error}")


# =========================
# PUBLIC FUNCTIONS
# =========================
def chat_fast(system_prompt: str, user_prompt: str) -> str:
    """
    Cheap tasks:
    - gender detection
    - tag extraction
    - hook ranking
    """
    msgs = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    return _ask_with_fallback(msgs, CHEAP_PROVIDERS)


def chat_strong(system_prompt: str, user_prompt: str) -> str:
    """
    Expensive reasoning:
    - rewriting titles
    - creative hooks
    - summarization
    """
    msgs = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    # try strong models first
    try:
        return _ask_with_fallback(msgs, STRONG_PROVIDERS)
    except:
        # fallback to cheap if exhausted
        return _ask_with_fallback(msgs, ALL_PROVIDERS)