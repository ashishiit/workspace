'''
Created on Oct 10, 2018

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None
    def Insert(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next
l = LinkedList()
l.Insert(1)
l.Insert(2)
l.Insert(3)
l.Insert(4)
l.Insert(5)
l.Insert(6)
l.Display()