import time
import RPi.GPIO as gpio

p1=11
p2=15
p3=16
p4=18

def setUpGPIO():
    gpio.setmode(gpio.BOARD)
    gpio.setup(p1,gpio.OUT)
    gpio.setup(p2,gpio.OUT)
    gpio.setup(p3,gpio.OUT)
    gpio.setup(p4,gpio.OUT)


def stopAllMotors():    
    gpio.output(p1,False)
    gpio.output(p2,False)
    gpio.output(p3,False)
    gpio.output(p4,False)

def initEngine():
    gpio.setwarnings(False)
    setUpGPIO()
    stopAllMotors()

def motionForward(motionTime):
    print("Running Forward")
    gpio.output(p1,False)
    gpio.output(p2,True)
    gpio.output(p3,False)
    gpio.output(p4,True)
    time.sleep(motionTime)
    stopAllMotors()


def motionBackward(motionTime):
    print("Running Backward")
    gpio.output(p1,True)
    gpio.output(p2,False)
    gpio.output(p3,True)
    gpio.output(p4,False)
    time.sleep(motionTime)
    stopAllMotors()

    
def motionRight(motionTime):
    print("Running Right")
    gpio.output(p1,True)
    gpio.output(p2,False)
    gpio.output(p3,False)
    gpio.output(p4,True)
    time.sleep(motionTime)
    stopAllMotors()

def motionLeft(motionTime):
    print("Running Left")
    gpio.output(p1,False)
    gpio.output(p2,True)
    gpio.output(p3,True)
    gpio.output(p4,False)
    
    time.sleep(motionTime)
    stopAllMotors()





