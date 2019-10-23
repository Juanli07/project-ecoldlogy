import RCWL
import RPi.GPIO as GPIO
import motionSensor
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup
# instance = motionSensor.motionSensor(2)
# x = 0;
# while True:
#     x+=1
#     xd = instance.returnResults()
#     print("{}] {} ".format(x, xd))

instance = RCWL.rcwl(12)

while True:
     read = instance.returnResults
     print(read)

instance = dht11.DHT11(pin = 7)

while True:
    result  = instance.read()
    if result.is_valid():
        print("Temperatura : {}, Humedad : {}".format(result.temperature, result.humidity))
        time.sleep(2)

GPIO.cleanup()
