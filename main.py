import time
import picamera
import func

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    while True:
        func.isDifferent('image/0.jpg','image/1.jpg')
        # func.sendEmail("bryan35818363680919@gmail.com", 'image/1.jpg')
        
        camera.capture_sequence([
            'image/0.jpg',
            'image/1.jpg'
            ], use_video_port=True)
    
    camera.stop_preview()
