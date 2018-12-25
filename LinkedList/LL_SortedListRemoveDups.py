'''
Created on Dec 25, 2017

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def InsertLast(self,data):
        NewLink = Link(data)
        if self.last is None:
            self.first = NewLink
        else:
            self.last.next = NewLink
        self.last = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
    def Solution(self):
        previous = self.first
        current = self.first.next
        while current is not None:
            if previous.data == current.data:
                temp = current.next
                previous.next = temp
                current = temp
#                 current = current.next
            else:
                previous = current
                current = current.next
l = LinkedList()
l.InsertLast(11)
l.InsertLast(11)
l.InsertLast(11)
l.InsertLast(11)
l.InsertLast(12)
l.InsertLast(13)
l.InsertLast(13)
l.InsertLast(13)
l.Display()
l.Solution()
print()
l.Display()