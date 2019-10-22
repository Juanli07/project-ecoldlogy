
import motionSensor

instance = motionSensor.motionSensor(2)
x = 0;
while True:
    xd = instance.returnResults()
    print("{}] {} ".format(x+1, xd))


