'''
Created on Dec 21, 2018

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class List:
    def __init__(self):
        self.first = None
        
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    
    def Display(self):
        current = self.first
        while current is not None:
            print (current.data,end=" ")
            current = current.next
    
    def DeleteList(self):
        current = self.first
        while current is not None:
            Next = current.next
            del current.data
            current = Next
        self.first = current
l = List()
l.InsertFirst(2)
l.InsertFirst(45)
l.InsertFirst(34)
l.Display()
print('after deleting the entire list ',l.Display())