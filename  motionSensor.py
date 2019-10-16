import RPi.GPIO as GPIO
import time

class motionSensor:

    __pin = 0
    def __init__(self, pin):
        self.__pin = pin    

    
    def returnResults(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pin, GPIO.IN, GPIO.PUD_DOWN)
        time.sleep(1)
        status = GPIO.input(self.pin)
        return status;