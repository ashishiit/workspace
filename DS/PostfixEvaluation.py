'''
Created on Jun 3, 2017

@author: S528358
'''
class Stack:
    def __init__(self):
        self.a = []
    def Push(self, item):
        self.a.append(item)
    def Pop(self):
        return self.a.pop()
    def Peek(self):
        return self.a[len(self.a)-1]
    def isEmpty(self):
        return self.a == []
    def Size(self):
        return len(self.a)
    def Display(self):
        print(self.a)

def Solution(postfix):
    s = Stack()
    for i in postfix:
        if i in '0123456789':
            s.Push(i)
        else:
            b = int(s.Pop())
            a = int(s.Pop())
            if i == '*':
                s.Push(str(a*b))
            elif i == '/':
                s.Push(str(a/b))
            elif i == '+':
                s.Push(str(a+b))
            elif i == '-':
                s.Push(str(a-b))
    s.Display()
Solution('78+32+/')