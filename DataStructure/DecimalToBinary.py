'''
Created on May 24, 2017

@author: S528358
'''
class Stack:
    def __init__(self):
        self.a = []
    def Push(self,item):
        self.a.append(item)
    def Pop(self):
        return self.a.pop()
    def Peek(self):
        return self.a(len(self.a)-1)
    def Size(self):
        return len(self.a)
    def IsEmpty(self):
        return self.a == []

def Solution(inp):
    s = Stack()
    while inp != 0:
        s.Push(inp%2)
        inp = inp // 2
    s.a.reverse()
    print(s.a)
Solution(10)