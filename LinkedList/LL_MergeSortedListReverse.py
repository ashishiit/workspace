'''
Created on Jul 24, 2018

@author: S528358
'''
from tkinter.constants import CURRENT
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data,end=' ')
            current = current.next
    def Solution(self,current1,current2):
        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                l.InsertFirst(current1.data)
                current1 = current1.next
            else:
                l.InsertFirst(current2.data)
                current2 = current2.next
        while current1 is not None:
            l.InsertFirst(current1.data)
            current1 = current1.next
        while current2 is not None:
            l.InsertFirst(current2.data)
            current2 = current2.next
        current = l.first
        print()
        while current is not None:
            print(current.data,end=' ')
            current = current.next
l1 = LinkedList()
l1.InsertFirst(40)
l1.InsertFirst(15)
l1.InsertFirst(10)
l1.InsertFirst(5)
l1.Display()
print()
l2 = LinkedList()
l2.InsertFirst(20)
l2.InsertFirst(3)
l2.InsertFirst(2)
l2.Display()

l = LinkedList()
l.Solution(l1.first,l2.first)
