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
    def InsertFirst(self,data):
        NewLink = Link(data)
        NewLink.next = self.first
        self.first = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data,end=' ')
            current = current.next
    def Middle(self):
        total = 0
        current = self.first
        while current is not None:
            total = total + 1
            current = current.next
        previous = None
        slow = self.first
        fast = self.first.next.next
        while fast.next is not None:
            previous = slow
            slow = slow.next
            fast = fast.next
        temp = slow.next
        if total%2== 0:
            previous.next.next = None           
        else:
            previous.next = None
        
        print()
        print(self.first.data)
        rev = self.Reverse(temp)    
        print(rev.data)
        l1 = self.first
        l2 = rev
        while l1 is not None and l2 is not None:
            if l1.data != l2.data:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
#         print(slow.data)
    def Solution(self):
        return self.Middle()
    def Reverse(self,temp):
        current = temp
        NewLink = None
        while current is not None:
            link = current.next
            current.next = NewLink
            NewLink = current
            current = link
        temp = NewLink
        return temp

        
l = LinkedList()
l.InsertFirst(1)
l.InsertFirst(3)
l.InsertFirst(2)
l.InsertFirst(2)
l.InsertFirst(1)
l.Display()
result = l.Solution()
if result is True:
    print('it is palinddrome')
else:
    print('NOT a palindrome')