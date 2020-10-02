import backEngine as engine
import os
import time
import distanceMesaure
import threading


canGoForward=True

def initSetup():
    print("Setuping Assets ")
    engine.initEngine()
    
initSetup()


def keepGoingAhed():
    global canGoForward

    while True:
        if canGoForward==True:
            engine.motionForward(1)



def keepCheckingObst():
    global canGoForward
    while True:
        if distanceMesaure.getDist()>=0 and distanceMesaure.getDist()<=15:
            canGoForward=False
            engine.motionBackward(1)
            findNextDirection()
            break
        
def tiktok():
    global canGoForward
    time.sleep(10)
    canGoForward=False            
        
        
def findNextDirection():
    global canGoForward

    time.sleep(1.5)
    leftDist=0
    rightDist=0
    
    #Checking Left Dist
    engine.motionLeft(0.1)
    time.sleep(1)
    leftDist=distanceMesaure.getDist()
    
    #Checking Right Dist
    engine.motionRight(0.2)
    time.sleep(1)
    rightDist=distanceMesaure.getDist()
    
    if leftDist>rightDist:
        engine.motionLeft(1)
        
    canGoForward=True
    threading.Thread(target=keepCheckingObst).start()




threading.Thread(target=keepGoingAhed).start()
threading.Thread(target=keepCheckingObst).start()
threading.Thread(target=tiktok())
    
    






