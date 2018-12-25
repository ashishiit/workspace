'''
Created on Dec 22, 2017

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
            print(current.data)
            current = current.next
    def Middle(self):
        slow = self.first
        fast = self.first.next.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        print ('middle element = ', slow.data)
l = LinkedList()
l.InsertFirst(6)
l.InsertFirst(5)
l.InsertFirst(4)
l.InsertFirst(3)
l.InsertFirst(2)
l.InsertFirst(1)
l.Middle()