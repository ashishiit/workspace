'''
Created on Aug 2, 2018

@author: s528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def Insert(self,data):
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
    def Solution(self,l1,l2):
        current1 = l1
        current2 = l2
        while current1 is not None and current2 is not None:
            if current1.data == current2.data:
                l.Insert(current1.data)
                current1 = current1.next
                current2 = current2.next
            elif current1.data < current2.data:
                l.Insert(current1.data)
                current1 = current1.next
            else:
                l.Insert(current2.data)
                current2 = current2.next
        while current1 is not None:
            l.Insert(current1.data)
            current1 = current1.next
        while current2 is not None:
            l.Insert(current2.data)
            current2 = current2.next
l1 = LinkedList()
l2 = LinkedList()
l1.Insert(5)
l1.Insert(10)
l1.Insert(15)
l2.Insert(2)
l2.Insert(3)
l2.Insert(20)
l2.Insert(40)
l2.Insert(50)
l1.Display()
print()
l2.Display()
l = LinkedList()
l.Solution(l1.first,l2.first)
print()
l.Display()
