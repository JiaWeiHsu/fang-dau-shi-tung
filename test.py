import time
import picamera
import func

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    while True:

        camera.capture_sequence([
            'image/0.jpg',
            ], use_video_port=True)

    camera.stop_preview()
