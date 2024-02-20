import os
import ImageCapture as ic

if __name__ == '__main__':

    # Duration for which you want to run this script (for testing, changed to 10 seconds)
    # runTime = 24 * 60 * 60
    runTime = 60
    img_folder_name = 'data/img'
    video_folder_name = 'data/video'
    
    i=1
    runFolder = "run1"
    while os.path.exists(os.path.join(img_folder_name, runFolder)):
        i += 1
        runFolder = "run" + str(i)

    img_folder_name = os.path.join(img_folder_name, runFolder)
    video_folder_name = os.path.join(video_folder_name, runFolder)

    ic.CaptureImage(runFolder, runTime)

    # Check if the folder exists, if not, create it
    if not os.path.exists(video_folder_name):
        os.makedirs(video_folder_name)

    # ffmpeg command with the output file placed in the subfolder
    ffmpeg_command = f"ffmpeg -framerate 6 -pattern_type glob -i '{img_folder_name}/image_*.jpg' -c:v libx264 -pix_fmt yuv420p {video_folder_name}/timelapse.mp4"

    # Execute the ffmpeg command
    os.system(ffmpeg_command)
