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
    def InsertAfter(self,data, target):
        NewLink = Link(data)
        current = self.first
        while current.data != target:
            current = current.next
        NewLink.next = current.next
        current.next = NewLink
    def InsertLast(self,data):
        NewLink = Link(data)
        if self.first is None:
            self.first = NewLink
            return
        current = self.first
        while current.next is not None:
            current = current.next
        current.next = NewLink
        NewLink.next = None
    def Display(self):
        current = self.first
        while current is not None:
            print (current.data)
            current = current.next
l = LinkedList()
l.InsertLast(6)
l.InsertFirst(7)
l.InsertFirst(1)
l.InsertLast(4)
l.InsertAfter(8, 7)
l.Display()