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
    def InsertLast(self, data):
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
        a = []
        current = self.first
        previous = None
        
        while current is not None:
            if current.data not in a:
                a.append(current.data)
            elif current.data in a:
                Next = current.next
                previous.next = Next
                current = Next
            if current is None:
                return
            previous = current
            current = current.next
l = LinkedList()
l.InsertLast(11)
l.InsertLast(12)
l.InsertLast(13)
l.InsertLast(11)
l.InsertLast(14)
l.InsertLast(15)
l.InsertLast(16)
l.InsertLast(11)
l.Display()
print()
# sol = LinkedList()
l.Solution()
print('dups removed')
l.Display()