import RPi.GPIO as GPIO
import time

class motionSensor:

    __pin = 0
    def __init__(self, pin):
        self.__pin = pin    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pin, GPIO.IN, GPIO.PUD_DOWN)

    
    def returnResults(self):
        time.sleep(1)
        status = GPIO.input(self.__pin)
        return status