'''
Created on Nov 21, 2016

@author: s528358
'''
class Link:
    def __init__(self, data):
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
    def Middle(self):
        current1 = self.first
#         hare tortoise algorithm. one link moves 2 times fast than the slower link
        current2 = current1.next.next
        while current2.next is not None:
            current1 = current1.next
            current2 = current2.next
        return current1.data
    def DeleteList(self):
        current = self.first
        while current is not None:
            current = current.next
        self.first = current
    def NthNode(self, N):
        count = 1
        current = self.first
        while count != N and current is not None:
            current = current.next
            count = count + 1
        if count != N:
            return 'not found'
        else:
            return current.data
#     passing data as reference
#     def test(self, Link l):
#         print(l.data)
#     def Print_test(self):
#         l = Link(5)
#         self.test(l)
li = LinkedList()
li.InsertFirst(20)
li.InsertFirst(5)
li.InsertFirst(56)
li.InsertFirst(67)
li.InsertFirst(23)
# li.Print_test()
li.Display()
print('middle link = %d'%li.Middle())
print('Nth Node')
print(li.NthNode(1))
print('empty the list')
li.Display()