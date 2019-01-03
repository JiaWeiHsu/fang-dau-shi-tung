def buzzier():
    import time
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(50)
   
    p.ChangeFrequency(659)
    time.sleep(1)

    p.stop()
    GPIO.cleanup()

buzzier()
