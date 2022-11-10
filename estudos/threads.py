from threading import *    
import time  

def thread1() :                 
  for i in range(100) : 
    print("Ping")
    time.sleep(2)
    
     
def thread2() :                 
  for i in range(100) : 
    print("Pong")
    time.sleep(4)
      
Thread1 = Thread(target=thread1)         
Thread1.start()    

Thread2 = Thread(target=thread2)
Thread2.start()