from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight()

    print("This is the distance of " + str(SensorRangeRight()))

    if SensorRangeRight() > 50:
        print ("1")