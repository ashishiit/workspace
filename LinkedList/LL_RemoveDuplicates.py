'''
Created on Aug 5, 2018

@author: s528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.last = None
        self.first = None
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
            print(current.data,end=' ')
            current = current.next
    def Solution(self):
        previous = self.first
        current = previous.next
        
        while current is not None:
            if current.data == previous.data:
                Next = current.next
                previous.next = Next
                current = Next
#                 previous = Next
            else:
                previous = current
                current = current.next
l = LinkedList()
l.InsertLast(11)
l.InsertLast(11)
l.InsertLast(11)
l.InsertLast(11)
l.InsertLast(43)
l.InsertLast(43)
l.InsertLast(60)
l.Display()
l.Solution()
print()
l.Display()        