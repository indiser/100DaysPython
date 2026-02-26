import smtplib
import os
from dotenv import load_dotenv
import shutil
import glob

load_dotenv()

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_APP_PASSWORD = os.environ.get("EMAIL_APP_PASS")

def send_alert(video_count):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        formatted_msg = f"""Your Viral Brainrot Factory has successfully generated {video_count} videos.
They have been packaged and moved to the 'ready_to_upload' folder.
It is time to drag and drop them into the TikTok/YouTube scheduler."""
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_APP_PASSWORD)
        
        msg = f"Subject: FACTORY ALERT: Weekly Batch Ready\n\n{formatted_msg}"
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=EMAIL_USER,
            msg=msg.encode('utf-8')
        )

if __name__ == "__main__":
    os.makedirs("ready_to_upload", exist_ok=True)
    finished_videos = glob.glob("reels/*.mp4")
    
    if len(finished_videos) >= 7:
        for video in finished_videos:
            filename = os.path.basename(video)
            shutil.move(video, f"ready_to_upload/{filename}")
        
        try:
            send_alert(len(finished_videos))
            print(f"✅ Batch ready! {len(finished_videos)} videos moved and alert sent.")
        except Exception as e:
            print(f"❌ Email failed: {e}")
    else:
        print(f"Current inventory: {len(finished_videos)}/7. Holding batch.")

