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
        self.last = None
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
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
        even = LinkedList()
        odd = LinkedList()
       
        current = self.first
        while current is not None:
            if current.data%2 == 0:
                even.InsertLast(current.data)
            else:
                odd.InsertLast(current.data)
            current = current.next
        print(even.first.data)
        print(odd.first.data)
        
        current1 = even.first
        current2 = odd.first
        temp = current1
        while current1.next is not None:
            current1 = current1.next
            
        current1.next = current2
        
        while temp is not None:
            print(temp.data,end=' ')
            temp = temp.next       
        
l = LinkedList()
l.InsertLast(8)
l.InsertLast(10)
l.InsertLast(5)
l.InsertLast(12)
l.InsertLast(12)
l.InsertLast(7)
l.InsertLast(10)

l.InsertLast(4)
l.InsertLast(1)

l.InsertLast(6)
l.Display()
print()
l.Solution()