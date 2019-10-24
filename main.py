import RCWL
import RPi.GPIO as GPIO
import motionSensor
import dht11
import time
import led
from datetime import date, datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup
try:
    ledon = led.led(12, 10)
    ledon.onLed()
    # instance = motionSensor.motionSensor(11)
    # x = 0;
    # while True:
    #     x+=1
    #     xd = instance.returnResults()
    #     print("{}] {} ".format(x, xd))

    #instance = RCWL.rcwl(13)

    #while True:
    #     read = instance.returnResults
    #     print(read)

    instance = dht11.DHT11(pin = 7)

    while True:
        result  = instance.read()
        if result.is_valid():
            print("Temperatura : {}, Humedad : {}, {}".format(result.temperature, result.humidity, datetime.now()))
            time.sleep(2)

    GPIO.cleanup()
except KeyboardInterrupt:
    print('\nSaliendo...')
    GPIO.cleanup()
finally:
    GPIO.cleanup()