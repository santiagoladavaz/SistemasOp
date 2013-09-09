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
        while(True):
            self.queue.put(self.num)
        
       
       
       
  
class threadR(threading.Thread): 
    def __init__(self,unNum,unaQueue):
        threading.Thread.__init__(self)
        self.num=unNum
        self.queue=unaQueue
    
    def run(self):
        while(True):
            print("Thread numero "+str(self.queue.get()))



if __name__ == "__main__":
    queue=Queue()
    t1=threadW("1",queue)
    t2=threadR("2",queue)
    t3=threadW("3",queue)
    t4=threadR("4",queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start() 