'''
Created on Jul 20, 2018

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
        count = 0
        current = self.first
        while current is not None:
            count = count + 1
            current = current.next
        return count
l = LinkedList()
l.InsertFirst(7)
l.InsertFirst(1)
l.InsertFirst(3)
l.InsertFirst(2)
l.InsertFirst(8)
l.Display()
print('length of list is = ',l.Solution())