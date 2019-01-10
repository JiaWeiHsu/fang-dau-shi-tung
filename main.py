import time
import picamera
import func

count = -1
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.rotation = 90
    time.sleep(2)
    while True:

        camera.capture_sequence([
            'image/0.jpg',
            ], use_video_port=True)

        tmp = func.countObj()  
        
        if count != tmp and count != -1:
            func.buzzier()

        count = tmp

    camera.stop_preview()
