'''
Created on 02/09/2013

@author: Santi
'''
import threading 

class thread(threading.Thread):
    
    def __init__(self,unNum,unaLista):
        threading.Thread.__init__(self)
        self.num=unNum
        self.lista=unaLista
    
    def run(self):
        self.lista.pop(0)
        for p in range(len(self.lista)):
            print("Soy el thread numero "+str(self.num)+ " e imprimo el elemento num: "+ str(p));
            
           
           
if __name__ == "__main__":
    miLista=['HOLA', 'MUNDO', 'CHAU']
    t1=thread("1",miLista)
    t2=thread("2",miLista)
    t3=thread("3",miLista)
    t4=thread("4",miLista)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    