from db import accessToDB
import motionSensor

instance = motionSensor.motionSensor(2)

while(xd != 0):
    xd = instance.returnResults()


