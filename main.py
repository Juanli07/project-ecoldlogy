
import motionSensor

instance = motionSensor.motionSensor(2)
x = 0;
while True:
    x+=1
    xd = instance.returnResults()
    print("{}] {} ".format(x, xd))


