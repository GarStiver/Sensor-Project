import distance
import distanceRight

while True:
    distance.SensorRangeLeft()
    distanceRight.SensorRangeRight()

    #Vasemman laskeminen
    if(distance.SensorRangeLeft().distanceLeftC < 50):
        if(distanceRight.SensorRangeRight().distanceRightC < 50):
            print ("1")