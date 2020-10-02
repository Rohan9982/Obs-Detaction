import time
import threading




def keepGoingAhed():
    global b
    b = 3
    a = True
    while a:
        print("Hello")
        time.sleep(2)
        b = 2
    
    print(b)

   
abc = threading.Thread(target=keepGoingAhed).start()
abc.join(2)

