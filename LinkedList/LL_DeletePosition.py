'''
Created on Dec 21, 2017

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
    def Delete(self,position):
        position = position-1
        previous = None
        current = self.first
        for i in range(position):
            previous = current
            current = current.next
        if previous is None:
            self.first = self.first.next
        else:
            previous.next = current.next
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next
l = LinkedList()
l.InsertFirst(8)
l.InsertFirst(2)
l.InsertFirst(3)
l.InsertFirst(1)
l.InsertFirst(7)
l.Display()
print('++++++====')
l.Delete(4)
l.Display()