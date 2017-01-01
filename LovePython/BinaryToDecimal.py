'''
Created on Dec 18, 2016

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.next = None
        self.data = data
class BinaryToDecimal:
    def __init__(self):
        self.first = None
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next
    def Solution(self):
        current = self.first
        result = 0
        while current is not None:
            result = (result*2) + current.data
            current = current.next
        return result            
l = BinaryToDecimal()
l.InsertFirst(1)
l.InsertFirst(0)
l.InsertFirst(1)
l.Display()
print('decimal value = %d'%l.Solution())