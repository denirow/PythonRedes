from threading import *    
import time  

def thread1() :                 
  for i in range(10) : 
    print("Ping")
    
     
def thread2() :                 
  for i in range(10) : 
    print("Pong")
    
      
Thread1 = Thread(target=thread1)         
Thread1.start()    

Thread2 = Thread(target=thread2)
Thread2.start()