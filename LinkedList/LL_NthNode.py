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
    def NthNode(self,position):
        current = self.first
        for i in range(position):
            current = current.next
        print(current.data)
l = LinkedList()
l.InsertFirst(14)
l.InsertFirst(30)
l.InsertFirst(10)
l.InsertFirst(1)
l.NthNode(1)            