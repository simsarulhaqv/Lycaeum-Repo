class Stack :
    def __init__(self) :
        self.item=[]
    def push(self,value) :
        self.item = self.item.append(value)
    def pop(self) :
        return self.item.pop()
    def isEmpty(self) :
        return self.item == []
