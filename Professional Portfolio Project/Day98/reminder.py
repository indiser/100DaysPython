import smtplib
import os
from dotenv import load_dotenv
import shutil,glob

load_dotenv()

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_APP_PASSWORD = os.environ.get("EMAIL_APP_PASS")

def sent_alert(video_count):
    with smtplib.SMTP("smtp.gmail.com",587) as connections:
        formatted_msg=f"""Your Viral Brainrot Factory has successfully generated {video_count} videos.
        They have been packaged and moved to the 'ready_to_upload' folder.
        It is time to drag and drop them into the TikTok/YouTube scheduler."""
        connections.starttls()
        connections.login(user=EMAIL_USER,password=EMAIL_APP_PASSWORD)
        connections.sendmail(
            from_addr=EMAIL_USER,
            to_addrs="ingenral219@gmail.com",
            msg=f"Subject:🟢 FACTORY ALERT: Weekly Batch Ready\n\n{formatted_msg}"
        )

os.makedirs("ready_to_upload", exist_ok=True)
finished_videos=glob.glob("reels/*.mp4")
if len(finished_videos) >= 7:
    
    for video in finished_videos:
        filename=os.path.basename(video)
        shutil.move(video,f"ready_to_upload/{filename}")

    try:
        sent_alert(len(finished_videos))
    except:
        print("Messege Failed")
else:
    print(f"Current inventory: {len(finished_videos)}/7. Holding batch.")

