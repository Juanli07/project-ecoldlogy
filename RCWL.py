from gpiozero import DigitalInputDevice

class rcwl:

    __pin = 0;

    def __init__(self, pin):
        self.__pin = pin

    
    def returnResults(self):
        radar = DigitalInputDevice(self.__pin, pull_up=False, bounce_time=2.0)
        if(radar.when_activated):
            r = 1
            return r 
        else:
            r = 0
            return r


