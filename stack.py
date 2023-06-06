class stack :
    def __init__(self) :
        self.stack = []
        
    def addfront(self,item) :
        self.stack.insert(0,item)
        
    def addrear(self,item) :
        self.stack.append(item)
        
    def removefront(self) :
        self.stack.pop()
        
    def removerear(self) :
        self.stack.pop(0)
     
    def isempty(self) :
        if self.stack == [] :
            return True
        else :
            return False
    
    def size(self) :
        return len(self.stack)

    def reverse(self):
        try :            
            data = self.stack[0]
            reversedlist = []
            
            triger = len(data)
            for x in range(triger) :
                reversedlist.append(data[triger-1])
                triger -= 1
                
            return reversedlist
        
        except :
            return False
        
