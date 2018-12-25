'''
Created on Jul 21, 2018

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
            print(current.data,end=' ')
            current = current.next
    def Solution(self):
        previous = None
        current = self.first
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        current.next = self.first
        self.first = current
l = LinkedList()
l.InsertFirst(13)
l.InsertFirst(12)
l.InsertFirst(15)
l.InsertFirst(10)
l.Display()
print()
l.Solution()
l.Display()