'''
Created on 26/08/2013

@author: Publico
'''


class program():
    
    def __init__(self):
        self.instructions=[]
        
    def addIns(self,ins):
        self.instructions.append(ins)
    
        
    def countIns(self):
        self.printIns()
        return len(self.instructions);
     
    def printIns(self):
        for ins in self.instructions:
            print(ins)




