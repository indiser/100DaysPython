import os
import json
import glob
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
script_path=os.path.dirname(os.path.abspath(__file__))
credentials_path=os.path.join(script_path,"client.json")
scripts_path=os.path.join(script_path,"scripts.json")

def get_authenticated_service():
    """Authenticate and return the YouTube API service."""
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server()
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

def get_video_metadata(video_id):
    """Get metadata from scripts.json for a video ID."""
    with open(scripts_path, "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    for script in scripts:
        if script["posted_youtube"] == True:
            continue
        if script["id"] == video_id:
            return script
    return None

def mark_as_posted(video_id):
    """Saves the 'posted' status back to the physical database."""
    with open(scripts_path, "r", encoding="utf-8") as f:
        scripts = json.load(f)
        
    for script in scripts:
        if script["id"] == video_id:
            script["posted_youtube"] = True
            break
            
    with open(scripts_path, "w", encoding="utf-8") as f:
        json.dump(scripts, f, indent=4, ensure_ascii=False)

def upload_video(file_path, metadata):
    """Uploads a video to YouTube with metadata from scripts.json."""
    youtube = get_authenticated_service()

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    # Build title and description from metadata
    raw_hook = metadata['hook']
    if len(raw_hook) > 92:
        raw_hook = raw_hook[:89] + "..."

    title = f"{raw_hook} #Shorts"
    raw_tags = metadata["tags"]

    clean_tags=[]
    for tag in raw_tags:
        if isinstance(tag,str):
            word_count=len(tag.split())
            char_count=len(tag)
            if word_count <= 6 and char_count <= 35:
                clean_tags.append(tag)
        else:
            continue

    hashtag_string = ' '.join(['#' + tag.replace(' ', '') for tag in clean_tags])
    description = (
        f"{metadata['hook']}\n\n"
        f"Wait until you hear how this ends... 💀\n\n"
        f"Who do you think is actually in the wrong here? Let me know your thoughts in the comments! 👇\n\n"
        f"{hashtag_string} #RedditStories #StoryTime"
    )
    
    body = {
        "snippet": {
            "title": title,  # YouTube title limit
            "description": description[:5000],  # YouTube description limit
            "tags": clean_tags + ["Shorts", "YouTubeShorts", "RedditStories"],
            "categoryId": "24"  # Entertainment
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

    try:
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()
        print(f"✅ Uploaded: {metadata['id']} | Video ID: {response['id']}")
        mark_as_posted(video_id=metadata['id'])
        return True
    except HttpError as e:
        print(f"❌ Upload failed for {metadata['id']}: {e}")
        return False

if __name__ == "__main__":
    # Get all videos from ready_to_upload folder
    video_files = glob.glob("ready_to_upload/*.mp4")
    
    if not video_files:
        print("No videos found in ready_to_upload/ folder")
    else:
        print(f"Found {len(video_files)} videos to upload\n")
        
        success_count = 0
        for video_path in video_files:
            # Extract video ID from filename (format: Title_words_ID.mp4)
            filename = os.path.basename(video_path)
            video_id = filename.replace(".mp4", "").split("_")[-1]
            
            # Get metadata from scripts.json
            metadata = get_video_metadata(video_id)
            
            if metadata:
                print(f"Uploading: {filename}")
                if upload_video(video_path, metadata):
                    success_count += 1
                print()
            else:
                print(f"⚠️ No metadata found for {video_id}, skipping\n")
        
        print(f"\n{'='*50}")
        print(f"Upload complete: {success_count}/{len(video_files)} successful")
