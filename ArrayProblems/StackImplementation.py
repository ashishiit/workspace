'''
Created on Oct 15, 2018

@author: S528358
'''
class Stack:
    def __init__(self,n):
        self.a = [None]*n
        self.size = n
        self.top = 0
    def Push(self,item):
        if self.top < self.size:
            self.a[self.top] = item
            self.top = self.top + 1
        else:
            print('overflow')
    def Pop(self):
        temp = self.a[self.top]
        self.top = self.top - 1
        return temp
    def Display(self):
        for i in self.a:
            print(i)
    def Peek(self):
        return self.a[self.top]
s = Stack(3)
s.Push(1)
s.Push(2)
s.Push(3)
s.Display()
s.Push(45)