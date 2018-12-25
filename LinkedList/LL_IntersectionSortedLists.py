'''
Created on Jul 22, 2018

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
    def Solution(self,l1,l2):
#         print(l1.data)
#         print(l2.data)
        current1 = l1
        current2 = l2
        while current1 is not None and current2 is not None:
            if current1.data == current2.data:
                l.InsertFirst(current1.data)
                current1 = current1.next
                current2 = current2.next
            elif current1.data < current2.data:
                current1 = current1.next
            elif current2.data < current1.data:
                current2 = current2.next
    
l1 = LinkedList()

l2 = LinkedList()
l1.InsertFirst(6)
l1.InsertFirst(4)
l1.InsertFirst(3)
l1.InsertFirst(2)
l1.InsertFirst(1)

l2.InsertFirst(8)
l2.InsertFirst(6)
l2.InsertFirst(4)
l2.InsertFirst(2)

l1.Display()
print()
l2.Display()

l = LinkedList()
print()
l.Solution(l1.first,l2.first)
print()
l.Display()