import os
import pysrt
import json

# 1. THE OVERRIDE MUST HAPPEN BEFORE MOVIEPY INITIALIZES
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"

import random
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
import moviepy.video.fx.all as vfx # WE NEED THIS FOR THE MATH
import random



def generate_subtitle_clips(json_path: str, video_width: int, video_height: int):
    """Reads word-level telemetry and groups them into perfectly synced chunks."""
    print("PARSING WORD-LEVEL TELEMETRY MATRIX...")
    
    with open(json_path, "r", encoding="utf-8") as f:
        words_data = json.load(f)
        
    sub_clips = []
    chunk_size = 3 # 2 words per pop-up
    
    for i in range(0, len(words_data), chunk_size):
        chunk = words_data[i:i+chunk_size]
        if not chunk:
            continue
            
        # The ultimate sync fix: exact start of first word, exact end of last word
        start_time = chunk[0]["start"]
        end_time = chunk[-1]["end"]
        chunk_text = " ".join([w["word"] for w in chunk])
        
        txt_clip = TextClip(
            chunk_text,
            font="Impact",
            fontsize=85, 
            color="white", 
            stroke_color="black",
            stroke_width=5,
            method="caption", 
            size=(video_width * 0.9, None) 
        )
        
        txt_clip = txt_clip.set_start(start_time).set_end(end_time).set_position(("center", video_height * 0.35))
        txt_clip = txt_clip.fx(vfx.resize, lambda t: 1 + 0.2 * max(0, (0.1 - t) * 10))

        # txt_clip = TextClip(
        #     chunk_text,
        #     font="Impact",
        #     fontsize=110,              # Bigger
        #     color="white",            # More eye-catching than white
        #     stroke_color="black",
        #     stroke_width=8,            # Thicker outline
        #     method="caption", 
        #     size=(video_width * 0.85, None)  # Slightly narrower for padding
        # )

        # txt_clip = txt_clip.set_start(start_time).set_end(end_time).set_position(("center", video_height * 0.70))
        # txt_clip = txt_clip.fx(vfx.resize, lambda t: 1 + 0.4 * max(0, (0.15 - t) * 6.67))  # Stronger pop

        sub_clips.append(txt_clip)
    return sub_clips

def build_viral_short(background_path: str, audio_path: str, json_path: str, output_path: str, test_mode: bool = False):
    print("ASSEMBLING VIDEO MATRIX...")
    
    video = VideoFileClip(background_path)
    audio = AudioFileClip(audio_path)
    video = video.without_audio()
    
    max_start_time = video.duration - audio.duration
    if max_start_time < 0:
        raise ValueError("CRITICAL: Background video is too short!")
        
    start_time = random.uniform(0, max_start_time)
    video = video.subclip(start_time, start_time + audio.duration)
    video = video.set_audio(audio)
    
    # The Vertical Crop
    w, h = video.size
    target_width = int((h * 9) / 16)
    x_center = w / 2
    video = video.crop(x1=x_center - target_width/2, y1=0, x2=x_center + target_width/2, y2=h)

    # --- THE NEW COMPOSITOR INJECTION ---
    # Generate the list of text layers based on the cropped screen size
    text_layers = generate_subtitle_clips(json_path, target_width, h)
    
    print("COMPOSITING LAYERS...")
    # Smash the video and text layers together into one final object
    final_video = CompositeVideoClip([video] + text_layers)

    print("INITIATING HARDWARE RENDER...")

    if test_mode:
        print("⚠️ TEST MODE ENGAGED: Slicing render timeline to 10 seconds...")
        # We use min() just in case the actual audio is somehow shorter than 10 seconds
        final_video = final_video.subclip(0, min(10, final_video.duration))
        

    # Render parameters remain heavily optimized to prevent your rig from dying
    final_video.write_videofile(
        output_path, 
        fps=30, 
        codec="libx264", 
        audio_codec="aac", 
        preset="ultrafast", 
        threads=1 
    )
    
    print(f"PIPELINE COMPLETE: Final output saved to {output_path}")
