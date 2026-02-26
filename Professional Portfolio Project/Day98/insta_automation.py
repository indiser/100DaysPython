# Instagram Reels Upload Automation (Instagram Graph API)
# 
# SETUP INSTRUCTIONS:
# 1. Install requests: pip install requests
# 2. Create Facebook Developer Account: https://developers.facebook.com/
# 3. Create a new app with Instagram Graph API access
# 4. Convert Instagram account to Business/Creator account
# 5. Link Instagram account to Facebook Page
# 6. Get long-lived access token from Graph API Explorer
# 7. Add to .env file:
#    INSTAGRAM_ACCESS_TOKEN=your_long_lived_token
#    INSTAGRAM_BUSINESS_ACCOUNT_ID=your_account_id
# 8. Upload videos to public hosting (AWS S3, Cloudinary, etc.)
# 
# USAGE:
# python insta_automation.py
# 
# IMPORTANT NOTES:
# - Instagram Graph API requires videos to be hosted on a PUBLIC URL
# - You must upload videos to S3/Cloudinary first, then pass the URL to the API
# - This script assumes you have a video hosting solution set up
# - Reels requirements: 9:16 aspect ratio, 4-60 seconds, max 1GB, H.264 codec
# - Rate limits: ~25 API calls per user per hour
# - Publishing takes 30-60 seconds for Instagram to process video

import os
import json
import glob
import time
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN")
BUSINESS_ACCOUNT_ID = os.environ.get("INSTAGRAM_BUSINESS_ACCOUNT_ID")
GRAPH_API_URL = "https://graph.facebook.com/v21.0"

def get_video_metadata(video_id):
    """Get metadata from scripts.json for a video ID."""
    with open("scripts.json", "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    for script in scripts:
        if script["id"] == video_id:
            return script
    return None

def upload_reel(video_url, metadata):
    """Upload a reel to Instagram using Graph API."""
    
    # Build caption from metadata
    caption = f"{metadata['hook']}\n\n{' '.join(['#' + tag.replace(' ', '') for tag in metadata['tags']])} #fyp #viral"
    
    # Step 1: Create media container
    container_url = f"{GRAPH_API_URL}/{BUSINESS_ACCOUNT_ID}/media"
    container_params = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption[:2200],  # Instagram caption limit
        "access_token": ACCESS_TOKEN
    }
    
    try:
        response = requests.post(container_url, params=container_params)
        response.raise_for_status()
        container_id = response.json()["id"]
        print(f"   Container created: {container_id}")
        
        # Step 2: Wait for video processing
        print("   Waiting for Instagram to process video...")
        time.sleep(30)
        
        # Step 3: Publish the container
        publish_url = f"{GRAPH_API_URL}/{BUSINESS_ACCOUNT_ID}/media_publish"
        publish_params = {
            "creation_id": container_id,
            "access_token": ACCESS_TOKEN
        }
        
        response = requests.post(publish_url, params=publish_params)
        response.raise_for_status()
        media_id = response.json()["id"]
        
        print(f"✅ Published: {metadata['id']} | Media ID: {media_id}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Upload failed for {metadata['id']}: {e}")
        return False

if __name__ == "__main__":
    print("\n⚠️  IMPORTANT: This script requires videos to be hosted on a PUBLIC URL")
    print("You must upload videos to AWS S3, Cloudinary, or similar service first.\n")
    print("Example workflow:")
    print("1. Upload ready_to_upload/*.mp4 to S3 bucket")
    print("2. Get public URLs for each video")
    print("3. Pass URLs to this script\n")
    
    # Get all videos from ready_to_upload folder
    video_files = glob.glob("ready_to_upload/*.mp4")
    
    if not video_files:
        print("No videos found in ready_to_upload/ folder")
    else:
        print(f"Found {len(video_files)} videos\n")
        print("To upload these to Instagram:")
        print("1. Upload each video to your hosting service")
        print("2. Call upload_reel(video_url, metadata) for each video\n")
        
        # Example usage (uncomment and modify when you have video URLs):
        # for video_path in video_files:
        #     filename = os.path.basename(video_path)
        #     video_id = filename.replace(".mp4", "").split("_")[-1]
        #     metadata = get_video_metadata(video_id)
        #     
        #     if metadata:
        #         # Replace with your actual video URL from S3/Cloudinary
        #         video_url = f"https://your-bucket.s3.amazonaws.com/{filename}"
        #         upload_reel(video_url, metadata)
        #         time.sleep(60)  # Rate limit protection
