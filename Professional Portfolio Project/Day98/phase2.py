import asyncio
import edge_tts
import random
import json

WOMAN_VOICE_LIST = [
    "en-US-JennyNeural",
    "en-US-MichelleNeural",
    "en-US-AriaNeural",
]


# async def generate_audio_and_subs(text: str, output_audio_path: str, output_srt_path: str, gender: str = "M"):
#     print(f"COMMENCING AUDIO GENERATION (Voice Profile: {gender})...")
    
#     # Dynamic Voice Routing
#     # Aria is a great, clear female AI voice. Christopher is the standard male.
#     voice_model = random.choice(WOMAN_VOICE_LIST) if gender == "F" else "en-US-GuyNeural"
    
#     communicate = edge_tts.Communicate(text, voice_model)
#     submaker = edge_tts.SubMaker()

#     with open(output_audio_path, "wb") as audio_file:
#         async for chunk in communicate.stream():
#             if chunk["type"] == "audio":
#                 audio_file.write(chunk["data"])
#             elif chunk["type"] in ["WordBoundary", "SentenceBoundary"]:
#                 submaker.feed(chunk)

#     with open(output_srt_path, "w", encoding="utf-8") as srt_file:
#         srt_file.write(submaker.get_srt())

#     print(f"SUCCESS: Saved {output_audio_path} and {output_srt_path}")

async def generate_audio_and_subs(text: str, output_audio_path: str, output_json_path: str, gender: str = "F"):
    print(f"COMMENCING AUDIO GENERATION (Voice Profile: {gender})...")
    
    voice_model = random.choice(WOMAN_VOICE_LIST) if gender == "F" else "en-US-ChristopherNeural"
    communicate = edge_tts.Communicate(text, voice_model)
    
    word_boundaries = []
    sentence_fallback = []

    with open(output_audio_path, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
                
            # 1. THE PRIMARY ENGINE: Try to catch the high-precision packets
            elif chunk["type"] == "WordBoundary":
                start_time = chunk["offset"] / 10000000.0
                end_time = (chunk["offset"] + chunk["duration"]) / 10000000.0
                word_boundaries.append({
                    "word": chunk["text"],
                    "start": start_time,
                    "end": end_time
                })
                
            # 2. THE HEURISTIC SHIELD: Catch the sentence packets just in case
            elif chunk["type"] == "SentenceBoundary":
                start_time = chunk["offset"] / 10000000.0
                end_time = (chunk["offset"] + chunk["duration"]) / 10000000.0
                
                words = chunk["text"].split()
                if not words:
                    continue
                    
                # Mathematically distribute the time across the words
                chunk_duration = (end_time - start_time) / len(words)
                
                for i, word in enumerate(words):
                    sentence_fallback.append({
                        "word": word,
                        "start": start_time + (i * chunk_duration),
                        "end": start_time + ((i + 1) * chunk_duration)
                    })

    # 3. THE LOGIC GATE: Decide which data to trust
    if not word_boundaries:
        print("WARNING: Upstream API dropped WordBoundary packets. Deploying heuristic fallback.")
        final_telemetry = sentence_fallback
    else:
        # Sort just in case packets arrived out of order
        final_telemetry = sorted(word_boundaries, key=lambda x: x["start"])

    # 4. Save the surviving data to the JSON matrix
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(final_telemetry, json_file, indent=4, ensure_ascii=False)

    print(f"SUCCESS: Saved {output_audio_path} and telemetry to {output_json_path}")

