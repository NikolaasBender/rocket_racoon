import PRi.GPIO as GPIO
import time

class Servo:
    # Initialize servo
    # run test startup procedure
    # hz should be 50
    def __init__(self, pin, hz):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        servo = GPIO.PWM(pin, hz)
        servo.start(0)
        self.StartUp()
        

    # probably +- 90deg
    # the sg90 duty cycle range is between 2% and 12%
    def GoTo(self, angle):
        # Quick clipping to range
        angle = max(-90, min(angle, 90))

        # Turn the angle into a usable duty cycle for the servo 
        dc = 2 + ((angle + 90) / 18)
        self.servo.ChangeDutyCycle(dc)
        return


    # Start up sequence to check the servos
    def StartUp(self):
        self.GoTo(-90)
        time.sleep(0.5)
        self.GoTo(90)
        time.sleep(0.5)
        self.GoTo(-45)
        time.sleep(0.5)
        self.GoTo(45)
        time.sleep(0.5)
        self.GoTo(0)
        time.sleep(0.5)
        return
        