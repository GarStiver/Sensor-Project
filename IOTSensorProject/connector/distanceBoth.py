from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight(distanceRightC)

    print("This is the distance of " + str(distanceRightC))

    if distanceRightC > 50:
        print ("1")

