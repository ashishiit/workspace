'''
Created on Jul 19, 2018

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None
    def InserFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data,end=' ')
            current = current.next
    def Solution(self,position):
        start = 0
        previous = None
        current = self.first
        while start != position:
            previous = current
            current = current.next
            start = start + 1
        if previous is None:
            self.first = self.first.next
        else:
            previous.next = current.next
l = LinkedList()
l.InserFirst(7)
l.InserFirst(1)
l.InserFirst(3)
l.InserFirst(2)
l.InserFirst(8)
l.Display()
l.Solution(1)
print()
l.Display()