import RCWL
import motionSensor
import dht11
import time
# instance = motionSensor.motionSensor(2)
# x = 0;
# while True:
#     x+=1
#     xd = instance.returnResults()
#     print("{}] {} ".format(x, xd))

# instance = RCWL.rcwl(7)

# while True:
#     read = instance.returnResults
#     print(read+"\n")

instance = dht11.DHT11(12)

while True:
    result  = instance.read()
    print("Temperatura : {}, Humedad : {}".format(result.temperature, result.humidity))
    time.sleep(2)