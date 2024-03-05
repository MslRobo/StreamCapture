import os
import sys
import signal
import argparse
import ImageCapture as ic

def run(args):

    # Duration for which you want to run this script (for testing, changed to 10 seconds)
    # runTime = 24 * 60 * 60
    img_folder_name = os.path.join(args.output, 'img')
    video_folder_name = os.path.join(args.output, 'video')
    
    i=1
    runFolder = "run1"
    while os.path.exists(os.path.join(img_folder_name, runFolder)):
        i += 1
        runFolder = "run" + str(i)

    img_folder_name = os.path.join(img_folder_name, runFolder)
    video_folder_name = os.path.join(video_folder_name, runFolder)

    # Catches errors and keyboard interrupts so that final cleanup can take place
    try:
        ic.CaptureImage(runFolder, args.runtime, args.spf, args.source)
    except:
        print("An error has been raised")

    # Check if the folder exists, if not, create it
    if not os.path.exists(video_folder_name):
        os.makedirs(video_folder_name)

    # ffmpeg command with the output file placed in the subfolder
    ffmpeg_command = f"ffmpeg -framerate {args.fps} -pattern_type glob -i '{img_folder_name}/image_*.jpg' -c:v libx264 -pix_fmt yuv420p {video_folder_name}/timelapse.mp4"

    # Execute the ffmpeg command
    os.system(ffmpeg_command)

def parse_opt():
    parser = argparse.ArgumentParser(description='Live feed recorder')
    parser.add_argument('-s', '--source', type=str, help='Source of the live feed')
    parser.add_argument('--spf', default=1, type=float, help='How often you want a picture to be recorded / Seconds per frame. Default is 1')
    parser.add_argument('--fps', default=3, type=int, help='Video framerate')
    parser.add_argument('-r', '--runtime', default=30, type=int, help='Define runtime for the software in seconds, default runtime is 30 seconds')
    parser.add_argument('--output', default='data', type=str, help='Root directory for output files')

    args = parser.parse_args()

    return args




if __name__ == '__main__':
    args = parse_opt()

    run(args)