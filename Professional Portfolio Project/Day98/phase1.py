import requests
import json
import random
import os
import re
import asyncio
from dotenv import load_dotenv
from langdetect import detect, LangDetectException

load_dotenv()

script_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir,"scripts.json")
database = []
existing_ids = set()

if os.path.exists(file_path):
    with open(file_path, "r", encoding="UTF-8") as filp:
        try:
            database = json.load(filp)
            existing_ids = {item["id"] for item in database}
        except json.JSONDecodeError:
            # Failsafe: If the file is corrupted, wipe it and start fresh.
            print("WARNING: Database corrupted. Starting fresh.")


OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
LIMIT = 1000
# 1. Define your fallback hierarchy
SUBREDDITS = [
    "AmItheAsshole",
    "AITAH",               # The uncensored alternative to AITA
    "TrueOffMyChest",
    "confessions",
    "tifu",
    "pettyrevenge",        # High-satisfaction payoff stories
    "entitledparents",     # Massive engagement and rage-bait
    "MaliciousCompliance", # Clever revenge stories
    "EntitledPeople",
    "relationships"
]
headers = {
    "User-Agent": "Python:BrainrotBot:v1.1 (by /u/YourRedditUsername)"
}


def sanitize_text(raw_text: str) -> str:
    # 1. Strip rogue URLs first
    text = re.sub(r'http\S+', '', raw_text)
    text = re.sub(r'(?i)\bTL;?DR\b.*', '', text, flags=re.DOTALL)
    # 2. Dynamic Age/Gender Translation (e.g., "19F" -> "a 19 year old female")
    text = re.sub(r'\b(\d{2})[Ff]\b', r'a \1 year old woman', text)
    text = re.sub(r'\b(\d{2})[Mm]\b', r'a \1 year old man', text)
    text = re.sub(r'\b[Ff](\d{2})\b', r'a \1 year old woman', text)
    text = re.sub(r'\b[Mm](\d{2})\b', r'a \1 year old man', text)
    

    # 3. The Master Acronym Dictionary
    slang_map = {
        "AITA": "Am I the jerk",
        "AITAH": "Am I the jerk here",
        "WIBTA": "Would I be the jerk",
        "TIFU": "Today I messed up",
        "MC": "Malicious compliance",
        "gf": "girlfriend",
        "bf": "boyfriend",
        "SO": "significant other",
        "MIL": "mother in law",
        "FIL": "father in law",
        "SIL": "sister in law",
        "BIL": "brother in law",
        "EM": "entitled mom",
        "ED": "entitled dad",
        "EK": "entitled kid",
        "EP": "entitled parent",
        "OP": "the original poster",
        "idk": "I don't know",
        "tbh": "to be honest",
        "btw": "by the way",
        "tf": "the heck",
        "wtf": "what the heck"
    }
    
    # 4. Apply Word-Boundary Replacements
    for slang, replacement in slang_map.items():
        # \b ensures 'gf' doesn't trigger inside other words
        # re.IGNORECASE handles 'aita', 'AITA', and 'Aita' automatically
        pattern = r'\b' + re.escape(slang) + r'\b'
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
    return text


def detect_gender_llm(title: str, story_text: str) -> str:
    """Uses a free LLM to semantically infer the narrator's gender."""
    
    # We only need the first ~1000 characters to get the context. 
    # Sending the whole story wastes tokens.
    context_chunk = story_text[:1000]
    
    # The Prompt Engineering: Strict constraints.
    system_prompt = (
        "You are a text analyzer. Read the following Reddit story and determine the gender of the narrator (the 'I' character). "
        "Look for explicit tags (like 19F) OR context clues (like 'my husband', 'my boyfriend', 'pregnant', etc). "
        "If it is completely ambiguous, guess based on the statistical likelihood of the writing style. "
        "YOU MUST REPLY WITH EXACTLY ONE LETTER: 'M' for Male, or 'F' for Female. DO NOT OUTPUT ANY OTHER TEXT."
    )
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "openrouter/free",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Title: {title}\n\nStory: {context_chunk}"}
                ],
                "temperature": 0.0 # Force deterministic, non-creative outputs
            })
        )
        response.raise_for_status()
        
        # Extract the single letter
        ai_guess = response.json()["choices"][0]["message"]["content"].strip().upper()
        
        # Failsafe: Ensure the LLM didn't disobey instructions
        if ai_guess in ["M", "F"]:
            return ai_guess
        else:
            print(f"WARNING: LLM hallucinated an invalid response: {ai_guess}. Defaulting to F.")
            return "F"
            
    except Exception as e:
        print(f"LLM Gender Detection Failed: {e}. Defaulting to F.")
        return "F"

def generate_viral_hook(title: str, story_text: str) -> str:
    """Forces the LLM to rewrite a boring Reddit title into a high-retention hook."""
    context_chunk = story_text[:1000]
    
    system_prompt = (
        "You are a ruthless viral copywriter for TikTok and YouTube Shorts. "
        "Read the following Reddit title and story. Your job is to rewrite the title into a highly engaging, "
        "dramatic, and aggressive hook that will stop people from scrolling. "
        "RULES: \n"
        "1. It MUST be under 12 words.\n"
        "2. It MUST start with a strong phrase like 'Am I the jerk for...', 'I ruined...', 'My entitled...', etc.\n"
        "3. DO NOT use hashtags, emojis, or quotation marks.\n"
        "4. Output ONLY the hook. Absolutely no other text."
    )
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/free", 
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Title: {title}\n\nStory: {context_chunk}"}
                ],
                "temperature": 0.7 
            }
        )
        response.raise_for_status()
        
        # Extract the hook and strip any accidental quotes the LLM tries to add
        hook = response.json()["choices"][0]["message"]["content"].strip().replace('"', '').replace('*', '')
        
        # Failsafe: If the LLM completely hallucinates and writes a paragraph, fallback to the original
        if len(hook.split()) > 20:
            return title
            
        return hook
            
    except Exception as e:
        print(f"LLM Hook Generation Failed: {e}. Defaulting to original title.")
        return title
    
def fetch_brainrot_story(subreddit_name: str, existing_ids:set ) -> dict:
    api_url = f"https://www.reddit.com/r/{subreddit_name}/top.json?t=day&limit={LIMIT}"
    response = requests.get(url=api_url, headers=headers)
    response.raise_for_status()
    data = response.json()

    for child in data['data']['children']:
        id = child['data']['id']
        original_story = child['data']['selftext']
        original_title = child['data']['title']
        url = child['data']['url']
        words = original_story.split()
        story=sanitize_text(original_story)
        title=sanitize_text(original_title)
        
        if id in existing_ids:
            print(f"Skipping {id}: Already exists in database.")
            continue # Skip to the next story immediately

        if story in ["[removed]", "[deleted]", ""]:
            continue
        
        if 120 < len(words) < 200:
            try:
                # If the library detects anything other than English ('en'), we dump it.
                if detect(story) != 'en':
                    print(f"Skipping {id}: Foreign language detected.")
                    continue
            except LangDetectException:
                # If the text is so corrupted it can't figure out the language, trash it.
                print(f"Skipping {id}: Unreadable text format.")
                continue
            
            pov_gender = detect_gender_llm(title=title,story_text=story)
            viral_hook = generate_viral_hook(title=title, story_text=story)
            print(f"Voice assigned: {pov_gender}")
            return {
                "id" : id,
                "original_title":original_title,
                "title": title.replace("\n\n"," ").replace("\n"," "),
                "hook": viral_hook, 
                "original_story":original_story,
                "story": story.replace("\n\n"," ").replace("\n"," "),
                "gender": pov_gender,
                "url" : url
            }
            
    # If the loop finishes without returning, raise the alarm.
    raise ValueError(f"No viable stories found in r/{subreddit_name}.")


# --- The Master Execution (The Waterfall) ---

def load_from_local_database() -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError("CRITICAL: Backlog missing.")
        
    with open(file_path, "r", encoding="UTF-8") as filp:
        database = json.load(filp)
        
    for item in database:
        if item.get("used") is False:
            item["used"] = True 
            
            # Save the mutated state back to the disk
            with open(file_path, "w", encoding="UTF-8") as filp:
                json.dump(database, filp, indent=4, ensure_ascii=False)
                
            return {"id": item["id"], "title": item["title"], "story": item["story"]}
            
    raise ValueError("FATAL: Backlog is completely empty.")


