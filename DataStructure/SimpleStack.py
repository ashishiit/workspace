'''
Created on May 23, 2017

@author: S528358
'''
class Stack:
    def __init__(self):
        self.a = []
    def Push(self,item):
        self.a.append(item)
    def Pop(self):
        self.a.pop()
    def Peek(self):
        return self.a[len(self.a)-1]
    def isEmpty(self):
        return self.a == []
    def Display(self):
        print(self.a)
    def Size(self):
        return len(self.a)
s = Stack()
s.Push(4)
s.Push(9)
s.Push(1)
s.Push(-90)
s.Display()
s.Pop()
print('after popping 1 element')
s.Display()