'''
Created on Jun 20, 2018

@author: S528358
'''
class StackX:
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
    def is_balanced(self, s):
        balanced = True
        for i in s:
            if i == '(':
                self.Push(i)
            elif i == ')':
                if self.isEmpty():
                    balanced = False
                    break
                else:
                    temp = self.Pop()
                    if i==')' and temp!='(' :
                        balanced = False
                        break
        if self.isEmpty() == True and balanced==True:
            return True
        else:
            return False
s = StackX()
inp = '((()))'
result = s.is_balanced(inp)
if result is True:
    print('is balanced')
else:
    print('is NOT balanced')