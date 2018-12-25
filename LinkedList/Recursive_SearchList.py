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
            print(current.data, end=" ")
            current = current.next
    
    def Recursive_Search(self,target):
        result = self.Recursive_app(target, self.first)
        if result is None:
            print("element not found")
        else:
            print("element found")
        
    def Recursive_app(self,target,link):
        if link is None:
            return None
        elif target == link.data:
            return link
        return self.Recursive_app(target, link.next)

l = List()
l.InsertFirst(34)
l.InsertFirst(4)
l.InsertFirst(2)
l.Display()
l.Recursive_Search(25)