import yt_dlp
import sys
import os
import shutil

def check_dependencies():
    """
    Validates the system environment before execution.
    A script is only as good as the environment it runs in.
    """
    fatal_error = False

    # 1. Check for FFmpeg (Critical for muxing audio and video)
    if not shutil.which("ffmpeg"):
        print("❌ FATAL: FFmpeg is missing or not in your system PATH.")
        print("   -> Fix (Windows): Run 'winget install Gyan.FFmpeg' as Administrator.")
        fatal_error = True

    # 2. Check for a JS Runtime (Required for YouTube's anti-bot protections)
    if not shutil.which("deno") and not shutil.which("node"):
        print("⚠️ WARNING: No JavaScript runtime (Deno or Node.js) detected.")
        print("   -> yt-dlp requires this to bypass YouTube's signature extraction.")
        print("   -> Fix (Windows): Run 'winget install DenoLand.Deno' as Administrator.")
        print("   -> The script will attempt to continue, but downloads may fail.")
        print("-" * 50)

    if fatal_error:
        print("\n🚨 Execution aborted. Fix your missing dependencies and try again.")
        sys.exit(1)

def download_video(url, output_dir="downloads", audio_only=False):
    """
    Download a video or audio using yt-dlp.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)

        ydl_opts = {
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'quiet': False,
        }

        if audio_only:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            ydl_opts.update({
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
            })

        print(f"⏳ Starting download for: {url}\n")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\n✅ Download completed successfully!")

    except Exception as e:
        print(f"\n❌ Error during execution: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yt_downloader.py <URL> [--audio]")
        sys.exit(1)

    # Enforce environment checks before doing anything else
    check_dependencies()

    video_url = sys.argv[1]
    audio_flag = "--audio" in sys.argv
    download_video(video_url, audio_only=audio_flag)