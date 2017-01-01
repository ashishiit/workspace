'''
Created on Dec 18, 2016

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.next = None
        self.data = data
class Merge2SortedLists:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
#         self.first2 = None
    def InsertFirst(self,data):
        self.count = self.count + 1
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def InsertLast(self,data):
        self.count = self.count + 1
        NewLink = Link(data)
        if self.last is None:
            self.first = NewLink
        else:
            self.last.next = NewLink
        self.last = NewLink
    def Display(self):
        current1 = self.first
        while current1 is not None:
            print(current1.data)
            current1 = current1.next
    def Solution(self):
        print('length of first list = %d'%l1.count)
        print('lenght of second list = %d'%l2.count)
        l1.Display()
        print('*****************')
        l2.Display()
#         i = 0
#         j = 0
        current1 = l1.first
        current2 = l2.first
        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                l3.InsertLast(current1.data)
                current1 = current1.next
            elif current2.data<current1.data:
                l3.InsertLast(current2.data)
                current2 = current2.next
            else:
                print('third condition')
                current1 = current1.next
                current2 = current2.next
        while current1 is not None:
            l3.InsertLast(current1.data)
            current1 = current1.next
        while current2 is not None:
            l3.InsertLast(current2.data)
            current2 = current2.next
        print('elements is final list = %d'%l3.count)
        print(l3.Display())
l1 = Merge2SortedLists()
l1.InsertFirst(22)
l1.InsertFirst(4)
l1.InsertFirst(3)
l1.InsertFirst(2)
l1.InsertFirst(1)

l2 = Merge2SortedLists()
l2.InsertFirst(30)
l2.InsertFirst(20)
l2.InsertFirst(10)

l3 = Merge2SortedLists()
l3.Solution()
            
        
    
    