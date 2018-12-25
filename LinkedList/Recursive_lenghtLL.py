'''
Created on Dec 21, 2018

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.first = None
        
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
        
    def Display(self):
        current = self.first
        while current is not None:
            print (current.data,end=' ')
            current = current.next
            
    def lengthList(self):
        print('length = ',self.lengthApp(self.first))
        
    def lengthApp(self,link):
        if link is None:
            return 0
        else:
            return 1+ self.lengthApp(link.next)
l = List()
l.InsertFirst(2)
l.InsertFirst(56)
l.InsertFirst(34)
l.Display()
l.lengthList()
        