#!/usr/bin/python3
import os
import apt
import sys
import time
import subprocess

def vlc_installed():
    cache = apt.Cache()
    return cache['vlc'].is_installed

if not vlc_installed():
    print("Please install VLC before using this script")
    sys.exit()

recording_directory = "recordings"
# TODO add scraper to "find" stream url
# m3u8_url = input("Stream url:")
m3u8_url = "https://node.imgio.in/demo/birds.m3u8"
# filename = input("Filename for the recording (w/ extention):")
filename = "test.mp4"

root_directory = os.getcwd()
os.makedirs(recording_directory, exist_ok=True)
recording_desination = os.path.join(root_directory, recording_directory, filename)

vlc_command = f'vlc -vvv {m3u8_url} --sout "#transcode{{vcodec=h264,scale=Auto,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}}:file{{dst={recording_desination},no-overwrite}}" :http-user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"'
print("Starting process")
process = subprocess.Popen(f"exec {vlc_command}", stdout=subprocess.PIPE, shell=True)
# TODO set "timer" or datetime to sleep/poll to let record until time up
time.sleep(10)
process.terminate()
print("VLC process terminated")
