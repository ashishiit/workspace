'''
Created on Jun 3, 2017

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
        return self.a[len(self.a)-1]
    def isEmpty(self):
        return self.a == []
    def Display(self):
        print(self.a)
    def Size(self):
        return len(self.a)

def Solution(infix):
    s = Stack()
    output = []
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    prec[')'] = 1
    for i in infix:
        if i is '(':
            s.Push(i)
        elif i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            output.append(i)
        elif i is ')':
            out = s.Pop()
            while out != '(':
                output.append(out)
                out = s.Pop()
        else:
            while not s.isEmpty() and (prec[s.Peek()]>=prec[i]):
                output.append(s.Pop())
            s.Push(i)
        
    while not s.isEmpty():
        output.append(s.Pop())
        
    return ''.join(output)
# print(Solution('A+B*C'))
print(Solution('A*B+C*D'))
                
            