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
            flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

def get_video_metadata(video_id):
    """Get metadata from scripts.json for a video ID."""
    with open("scripts.json", "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    for script in scripts:
        if script["id"] == video_id:
            return script
    return None

def upload_video(file_path, metadata):
    """Uploads a video to YouTube with metadata from scripts.json."""
    youtube = get_authenticated_service()

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    # Build title and description from metadata
    title = f"{metadata['hook']} #Shorts"
    description = f"{metadata['story']}\n\nSource: {metadata['url']}\n\n{' '.join(['#' + tag for tag in metadata['tags']])}"
    
    body = {
        "snippet": {
            "title": title[:100],  # YouTube title limit
            "description": description[:5000],  # YouTube description limit
            "tags": metadata["tags"] + ["Shorts", "YouTubeShorts", "RedditStories"],
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
        print(f"   Watch: https://youtu.be/{response['id']}")
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
