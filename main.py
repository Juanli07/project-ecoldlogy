import RCWL
import motionSensor

# instance = motionSensor.motionSensor(2)
# x = 0;
# while True:
#     x+=1
#     xd = instance.returnResults()
#     print("{}] {} ".format(x, xd))

instance = RCWL.rcwl(7)

while True:
    read = instance.returnResults
    print(read+"\n")
