import RPi.GPIO as GPIO
import time

class led:
    __time = 0
    __pin = 0
    def __init__(self, pin, time):
        self.__time = time
        self.__pin = pin
        
    def onLed(self):
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.__pin, GPIO.OUT)
            band = 0
            while(band < self.__time):
                    GPIO.output(self.__pin, True)
                    time.sleep(1)
                    GPIO.output(self.__pin, False)
                    time.sleep(1)
                    band+=1
        except KeyboardInterrupt:
            print('\nSaliendo...')
            GPIO.cleanup()
        finally:
            GPIO.output(self.__pin, True)
