import time
import picamera
import func

count = -1
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    while True:

        camera.capture_sequence([
            'image/0.jpg',
            ], use_video_port=True)

        tmp = func.countObj('image/0.jpg')  
        
        # if count != tmp and count != -1:
        #     func.sendEmail('image/0.jpg', 'bryan35818363680919@gmail.com')

        count = tmp

    camera.stop_preview()
