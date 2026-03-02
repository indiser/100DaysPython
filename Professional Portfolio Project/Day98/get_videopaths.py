import glob
import os

script_dir=os.path.dirname(os.path.abspath(__file__))
videos=glob.glob("ready_to_upload/*.mp4")

def video_paths():
    return list(map(lambda filename: os.path.join(script_dir,filename),videos))

print(video_paths())