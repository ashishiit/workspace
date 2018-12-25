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
    def Solution(self,n):
        previous = self.first
        current = self.first
        for i in range(n-1):
            current = current.next
        print('test = ', current.data)
        while current.next is not None:
            previous = previous.next
            current = current.next
        print('Nth element = ', previous.data)
l = LinkedList()
l.InsertFirst(14)
l.InsertFirst(20)
l.InsertFirst(13)
l.InsertFirst(12)
l.InsertFirst(15)
l.InsertFirst(10)
l.Solution(5)