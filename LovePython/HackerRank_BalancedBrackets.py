'''
Created on Jan 7, 2017

@author: S528358
'''
class StackApp:
    def __init__(self):
        self.a = []
    def Push(self,data):
        self.a.append(data)
    def Pop(self):
        return self.a.pop()
    def IsEmpty(self):
        return self.a == []
s = StackApp()
inp = '{[()]}'
isBalanced = True
for i in inp:
    if i=='(' or i=='{' or i=='[':
        s.Push(i)
    elif i==')' or i=='}' or i==']':
        if s.IsEmpty():
            isbalanced = False
            break
        else:
            temp = s.Pop()
            if (i==')' and temp!='(') or (i=='}' and temp!='{') and (i==']' and temp!= '['):
                isBalanced = False
                break
if s.IsEmpty() is True and isBalanced is True:
    print('Balanced')
else:
    print('not balanced')
                

        