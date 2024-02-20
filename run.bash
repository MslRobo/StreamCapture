python ImageCapture.py
ffmpeg -framerate 1 -pattern_type glob -i 'image_*.jpg' -c:v libx264 -pix_fmt yuv420p timelapse.mp4
