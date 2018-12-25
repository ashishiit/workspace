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
    def Delete(self,target):
        previous = None
        current = self.first
        while current.data != target:
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
l.InsertFirst(7)
l.InsertFirst(3)
l.InsertFirst(1)
l.InsertFirst(2)
l.InsertFirst(2)
l.InsertFirst(2)
l.Display()
l.Delete(2)
print('+++++++')
l.Display()
l.Delete(3)
print('+++++++')
l.Display()