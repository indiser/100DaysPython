import os
import re
import json
import asyncio
import random
from phase1 import fetch_brainrot_story, load_from_local_database, SUBREDDITS, existing_ids, database, file_path
from phase2 import generate_audio_and_subs
from phase3 import build_viral_short
import glob
import ctypes

def prevent_sleep():
    if os.name == 'nt':
        try:
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)
        except: pass

prevent_sleep()


BACKGROUND_PATH_LIST=glob.glob("downloads/*.mp4")
TEST_MODE = False

def sanitize_filename(title: str, max_length: int = 50) -> str:
    """Removes illegal OS characters and spaces from the title."""
    # Strip illegal characters: \ / * ? " < > | :
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    # Replace spaces with underscores for clean URLs/paths
    clean = clean.replace(" ", "_")
    return clean[:max_length]

def main():
    print("=== INITIATING VIRAL FACTORY PIPELINE ===")
    
    # 1. Build the outputs directory if it doesn't exist
    os.makedirs("reels", exist_ok=True)
    
    todays_script = None

    random.shuffle(SUBREDDITS)
    # 2. The Ingestion Waterfall
    for sub in SUBREDDITS:
        print(f"Attempting to fetch from r/{sub}...")
        try:
            todays_script = fetch_brainrot_story(sub, existing_ids)
            print(f"SUCCESS: Secured story from r/{sub}.")
            
            todays_script["used"] = True
            database.append(todays_script)
            with open(file_path, "w", encoding="UTF-8") as filp:
                json.dump(database, filp, indent=4, ensure_ascii=False)
            break
        except Exception as e:
            print(f"FAILED on r/{sub}: {e} -> Pivoting to next source...")

    # 3. The Cold Storage Failsafe
    if not todays_script:
        print("CRITICAL: All live sources failed. Falling back to local cold storage...")
        todays_script = load_from_local_database()

    if todays_script:
        print("\n--- INGESTION COMPLETE ---")
        
        story_id = todays_script['id']
        # final_audio_script = f"{todays_script['title']}. {todays_script['story']}"
        final_audio_script = f"{todays_script.get('hook', todays_script['title'])}. {todays_script['story']}"
        
        # 4. Dynamic Uniqueness & Naming
        safe_title = sanitize_filename(todays_script['title'])
        audio_filename = f"audio_{story_id}.mp3"
        # srt_filename = f"subs_{story_id}.srt"
        json_filename = f"timestamps_{story_id}.json"
        
        # The target destination: reels/Clean_Title_ID.mp4
        final_video_filename = f"reels/{safe_title}_{story_id}.mp4"
        print(f"Target Video Path: {final_video_filename}")

        story_gender = todays_script.get('gender', 'F')
        
        # 5. Execute Phase 2: Audio & Subtitles
        asyncio.run(generate_audio_and_subs(final_audio_script, audio_filename, json_filename, story_gender))
        
        # 6. Execute Phase 3: Compositor
        # IMPORTANT: Make sure your background_path matches the actual filename in your folder
        build_viral_short(
            background_path=random.choice(BACKGROUND_PATH_LIST), 
            audio_path=audio_filename, 
            # srt_path=srt_filename,
            json_path=json_filename, 
            output_path=final_video_filename,
            test_mode=TEST_MODE
        )
        
        # 7. The Janitor (Cleanup)
        print("\n--- INITIATING CLEANUP ---")
        if os.path.exists(audio_filename):
            os.remove(audio_filename)
        # if os.path.exists(srt_filename):
        #     os.remove(srt_filename)
        if os.path.exists(json_filename): 
            os.remove(json_filename)
            
        print("Temporary assets deleted. Factory reset for tomorrow.")
        print(f"\n✅ PIPELINE 100% COMPLETE. Output secured at: {final_video_filename}")


if __name__ == "__main__":
    main()