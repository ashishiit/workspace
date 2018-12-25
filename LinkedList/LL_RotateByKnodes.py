'''
Created on Sep 16, 2018

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
            print(current.data)
            current = current.next
    def Solution(self,k):
        current = self.first
        for i in range(1,k):
            current = current.next
        temp = current.next
        current.next = None
        current = temp
        while current.next is not None:
            current = current.next
        current.next = self.first
        self.first = temp
        current = self.first
        while current is not None:
            print(current.data,end=' ')
            current = current.next
l = LinkedList()
l.Insert(10)
l.Insert(20)
l.Insert(30)
l.Insert(40)
l.Insert(50)
l.Insert(60)
l.Display()
k = int(input('enter value of k ?'))
l.Solution(k)
        