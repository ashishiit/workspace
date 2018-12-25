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
        current = self.first
        while current is not None and current.next is not None:
            temp = current.next.data
            current.next.data = current.data
            current.data = temp
            current = current.next.next
l = LinkedList()
l.InsertFirst(6)
l.InsertFirst(5)
l.InsertFirst(4)
l.InsertFirst(3)
l.InsertFirst(2)
l.InsertFirst(1)
l.Display()
print()
l.Solution()
l.Display()