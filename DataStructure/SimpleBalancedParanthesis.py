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
    def IsEmpty(self):
        return self.a == []
    def Size(self):
        return len(self.a)
    def Display(self):
        print(self.a)

def Solution(inp):
    s = Stack()
    isBalanced = True
    for i in inp:
        if i == '(':
            s.Push(i)
        elif i == ')':
            if s.IsEmpty() is True:
                isBalanced = False
                break
            else:
                s.Pop()
    if s.IsEmpty() and isBalanced:
        print('balanced')
    else:
        print('Not Balanced !!')
Solution('56890087))))')
Solution('((((56890087))))')