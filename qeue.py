class qeuee :
    def __init__(self) :
        self.qeue = []
        
    def addfront(self,item) :
        self.qeue.insert(0,item)
        
    def addrear(self,item) :
        self.qeue.append(item)
        
    def removefront(self) :
        self.qeue.pop()
        
    def removerear(self) :
        self.qeue.pop(0)
     
    def isempty(self) :
        if self.qeue == [] :
            return True
        else :
            return False
    
    def size(self) :
        return len(self.qeue)
