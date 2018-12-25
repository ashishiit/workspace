'''
Created on May 23, 2017

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
        if i=='(' or i=='{' or i=='[':
            s.Push(i)
        elif i==')' or i=='}' or i==']':
            if s.IsEmpty():
                isBalanced = False
                break
            else:
#                 print(s.Display())
                out = s.Pop()
#                 print(out)
                if (i==')' and out!='(') or (i=='}' and out!='{') or (i==']' and out!='['):
                    isBalanced = False
    
    if s.IsEmpty() and isBalanced:
        print('Balanced!')
    else:
        print('Not Balanced !!')
        
Solution('dfdfd}}})]]')
Solution('(fsd{fsd}jjhg)')