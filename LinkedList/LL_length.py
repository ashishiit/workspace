'''
Created on Dec 21, 2017

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
            print (current.data)
            current = current.next
    def Count_Link(self):
        num = 0
        current = self.first
        while current is not None:
            num = num + 1
            current = current.next
        print('# of links = ',num)
l = LinkedList()
l.InsertFirst(5)
l.InsertFirst(2)
l.InsertFirst(3)
l.Count_Link()