import RPi.GPIO as GPIO
import time
import Variables

GPIO.setmode(GPIO.BCM)

# Defining Trigger and Echo pin locations on Rasp
pinTriggerRight = 23
pinEchoRight = 24
dright = Variables.distanceRightC

# Setting up the trigger and echo pin Outputs and Inputs
GPIO.setup(pinTriggerRight, GPIO.OUT)
GPIO.setup(pinEchoRight, GPIO.IN)

# Counts the distance of the right sensor and return the value of dleft
def SensorRangeRight(dright):
    GPIO.output(pinTriggerRight, True)
    time.sleep(0.00001)
    GPIO.output(pinTriggerRight, False)
    startTime = time.time()
    stopTime = time.time()

    while 0 == GPIO.input(pinEchoRight):
        startTime = time.time()

    while 1 == GPIO.input(pinEchoRight):
        stopTime = time.time()

    TimeElapsed = stopTime - startTime

    dright = (TimeElapsed * 34300) / 2

    if dright < 2500:
        print ("DistanceRight: %.1f cm" % dright)
        time.sleep(0.5)

    return dright
