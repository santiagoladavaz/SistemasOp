'''
Created on 09/09/2013

@author: Santi
'''


import threading
from queue import Queue 

class threadW(threading.Thread):
    
    def __init__(self,unNum,unaQueue):
        threading.Thread.__init__(self)
        self.num=unNum
        self.queue=unaQueue
        
    
    def run(self):
        self.queue.put(self.num)
        
       
       
       
  
class threadR(threading.Thread): 
    
    def __init__(self,unNum,unaQueue):
        threading.Thread.__init__(self)
        self.num=unNum
        self.queue=unaQueue
    
    def run(self):
        print("Thread numero "+str(self.queue.get_nowait()))



if __name__ == "__main__":
    queue=Queue()
    t2=threadW("7",queue)
    t1=threadW("10",queue)
    t6=threadW("9",queue)
    t7=threadR("7",queue)
    t3=threadW("5",queue)
    t4=threadR("4",queue)
    t5=threadR("7",queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start() 
    t5.start()
    t6.start()
    t7.start()