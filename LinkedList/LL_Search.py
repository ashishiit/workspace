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
    def Search(self,target):
        current = self.first
        while current.data != target:
            current = current.next
            if current is None:
                return None
        return current
l = LinkedList()
l.InsertFirst(1)
l.InsertFirst(2)
l.InsertFirst(3)
l.InsertFirst(4)
l.InsertFirst(5)
result = l.Search(4)
if result is None:
    print('not found')
else:
    print('YES, FOUND.')