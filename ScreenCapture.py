import cv2
import time

# URL of the live feed
stream_url = 'https://straya.io/webcams/burnley-tunnel-east/'

# Open a connection to the stream
cap = cv2.VideoCapture(stream_url)

# Check if the stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open stream.")
    exit()

try:
    # Use 17280 for final stream
    for i in range(60):  # 1440 minutes in a day, change accordingly for different intervals
        ret, frame = cap.read()
        if ret:
            # Save frame as JPEG file
            cv2.imwrite(f"frame_{i}.jpg", frame)
            print(f"Captured frame {i}")
        else:
            print("Error: Could not read frame.")
        
        # Wait for 60 seconds (1 minute) before capturing the next frame
        time.sleep(5)
finally:
    cap.release()
