'''
Created on Oct 27, 2016

@author: s528358
'''
class Link:
    def __init__(self,item):
        self.next = None
        self.data = item
class OrderedList:
    def __init__(self):
        self.first = None
    def Insert(self,item):
        NewLink = Link(item)
        if self.first is None:
            self.first = NewLink
        else:
            previous = None
            current = self.first
            while current is not None and item > current.data:
                previous = current
                current = current.next
            if previous is None:
                self.first = NewLink
            else:
                previous.next = NewLink
            NewLink.next = current
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next
o = OrderedList()
o.Insert(30)
o.Insert(9)
o.Insert(67)
o.Insert(-1)
o.Display()    
                