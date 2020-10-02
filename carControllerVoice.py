import backEngine as engine
import socket
import os
import time

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

#Listening to socket
controllerSocket.listen(5)
clientSocket,addr=controllerSocket.accept()
print("Connected with ",addr)

while True:
    rdata=clientSocket.recv(1023).decode('utf-8')
    print("[+]Got Command....",rdata)
    
    if rdata=="forward":
        engine.motionForward(2)
        
    elif rdata=="backward":
        engine.motionBackward(2)
        
    elif rdata=="left":
        engine.motionLeft(0.5)
        
    elif rdata=="right":
        engine.motionRight(0.5)
        





