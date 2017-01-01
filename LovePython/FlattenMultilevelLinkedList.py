'''
Created on Dec 18, 2016

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.down = None
class FlattenLinkedList:
    def __init__(self):
        self.first = None
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next

    def Solution(self):
        print(l.first.next.data)
#         print(l2.first.data)
#         l1.first.next.down = l2.first
#         print(l1.first.next.down.data)
        
        
l = FlattenLinkedList()
l.first = Link(1)
l.first.next = Link(2)
l.first.next.next = Link(3)
l.first.next.next.next = Link(4)
l.first.next.next.next.next = None
l.first.next.down = Link(7)
l.first.next.down.next = Link(8)
l.first.next.down.next.next = Link(10)
l.first.next.down.next.next.next = Link(12)
l.first.next.down.next.next.next.next = None
l.first.next.down.down = Link(9)
l.first.next.down.next.down = Link(16)
l.first.next.down.next.next.down = Link(11)
l.first.next.down.down.down = Link(14)
l.first.next.down.next.down.down = Link(17)
l.first.next.down.next.down.down.next = Link(18)
l.first.next.down.next.down.down.next.next = Link(19)
l.first.next.down.next.dwon.down.next.next.next = Link(20)
l.first.next.down.next.down.down.next.next.next.next = None
l.first.next.down.down.down.down = Link(15)
l.first.next.down.down.down.down.next = Link(23)
l.first.next.down.down.down.down.next.down = Link(24)
l.first.next.down.next.down.down.next.next.next.down = Link(21)

l.Solution()
