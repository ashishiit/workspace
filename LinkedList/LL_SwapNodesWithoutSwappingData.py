'''
Created on Dec 22, 2017

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
    def SwapNodes(self,x,y):
        
l = LinkedList()
l.InsertFirst(14)
l.InsertFirst(20)
l.InsertFirst(13)
l.InsertFirst(12)
l.InsertFirst(15)
l.InsertFirst(10)
l.Display()