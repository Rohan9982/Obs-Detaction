import backEngine as engine
import socket
import os
import time
import threading
import distanceMesaure

controllerSocket=None

def initSetup():
    global controllerSocket
    print("Setuping Assets ")
    engine.initEngine()
    os.system("sudo fuser -k 9025/tcp")
    time.sleep(1)
    controllerSocket = socket.socket()
    controllerSocket.bind(('',9025))
    print "Setup Done , waitting for Incoming Connection..."

initSetup()

def keepCheckingObst():
    global canGoForward
    while True:
        distance=distanceMesaure.getDist()
        print(distance)
        if distance<=15:
            engine.stopAllMotors()
        time.sleep(0.25)


#Listening to socket
controllerSocket.listen(5)
clientSocket,addr=controllerSocket.accept()
print("Connected with ",addr)



threading.Thread(target=keepCheckingObst).start()



while True:
    rdata=clientSocket.recv(1023).decode('utf-8')
    print("[+]Got Command....",rdata)
    
    if rdata=="forward":
        engine.motionForward(5)
        
    elif rdata=="backward":
        engine.motionBackward(5)
        
    elif rdata=="left":
        engine.motionLeft(1)
        
    elif rdata=="right":
        engine.motionRight(1)
        







