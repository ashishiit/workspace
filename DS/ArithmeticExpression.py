'''
Created on Jun 4, 2017

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

def Calculate(postfix):
    new_s = Stack()
    for i in postfix:
        if i in '0123456789':
            new_s.Push(i)
        else:
            b = int(new_s.Pop())
            a = int(new_s.Pop())
            if i == '*':
                new_s.Push(str(a*b))
            elif i == '/':
                new_s.Push(str(a/b))
            elif i == '+':
                new_s.Push(str(a+b))
            elif i == '-':
                new_s.Push(str(a-b))
    print(int(new_s.Pop()))
            
def Solution(infix):
    s = Stack()
    output = []
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    for i in infix:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            output.append(i)
        elif i == '(':
            s.Push(i)
        elif i == ')':
            top = s.Pop()
            while top != '(':
                output.append(top)
                top = s.Pop()
        else:
            while not s.isEmpty() and prec[s.Peek()]>= prec[i]:
                output.append(s.Pop())
            s.Push(i)
    while not s.isEmpty():
        output.append(s.Pop())
#     print(output)
#     print(''.join(output))
    Calculate(output)
    
Solution('(2+3)*(4-1)')
            