import requests
import time
import os  # Import the os module

def CaptureImage(runFolder, runTime, spf, source):
    # URL of the picture that updates
    # picture_url = 'https://cmlwebcam.transurban.com/wimages/webcam03.jpg'
    picture_url = source

    # Name of the subfolder where you want to save the images
    img_folder_name = 'data/img'

    img_folder_name = os.path.join(img_folder_name, runFolder)

    # Check if the folder exists, if not, create it
    if not os.path.exists(img_folder_name):
        os.makedirs(img_folder_name)

    # Duration for which you want to run this script (for testing, changed to 10 seconds)
    # duration = 24 * 60 * 60
    duration = runTime

    # How often you want to download the picture in seconds
    interval = 1

    start_time = time.time()
    while (time.time() - start_time) < duration:
        # Current timestamp to use in the filename
        timestamp = int(time.time())
        response = requests.get(picture_url)
        if response.status_code == 200:
            # Modify filename to include the folder path
            filename = os.path.join(img_folder_name, f"image_{timestamp}.jpg")
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
        else:
            print("Failed to download image")

        # Wait for x seconds before downloading the next picture
        time.sleep(spf)
