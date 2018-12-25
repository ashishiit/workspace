'''
Created on Dec 24, 2017

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
            print (current.data, end = ' ')
            current = current.next
    def Solution(self,list_1,list_2):
#         print(list_1.data)
#         print(list_2.data)
        if list_1 is None:
            while list_2 is not None:
                self.InsertLast(list_2.data)
                list_2 = list_2.next
            return
        if list_2 is None:
            while list_1 is not None:
                self.InsertLast(list_1.data)
                list_1 = list_1.next
            return
        while list_1 is not None and list_2 is not None:
            if list_1.data < list_2.data:
                self.InsertLast(list_1.data)
                list_1 = list_1.next
            elif list_2.data < list_1.data:
                self.InsertLast(list_2.data)
                list_2 = list_2.next
            else:
                list_1 = list_1.next
                list_2 = list_2.next
        while list_1 is not None:
            self.InsertLast(list_1.data)
            list_1 = list_1.next
        while list_2 is not None:
            self.InsertLast(list_2.data)
            list_2 = list_2.next
            
list_1 = LinkedList()
list_1.InsertLast(1)
list_1.InsertLast(3)
list_1.InsertLast(5)
list_1.Display()
list_2 = LinkedList()
list_2.InsertLast(2)
list_2.InsertLast(4)
print()
list_2.Display()
print()
l = LinkedList()
l.Solution(list_1.first, list_2.first)
print('merged sorted lists')
l.Display()