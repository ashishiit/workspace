'''
Created on Oct 1, 2016

@author: S528358
'''
class StackPython:
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
    def Solution(self,s):
        balanced = True
        for i in s:
            if i == '(':
                self.Push(i)
            elif i == ')':
                print('checking this condition')
                print('check content of the Stack ', self.a)
                print('check emptiness or fullness of stack ',self.isEmpty())
                if self.isEmpty() == False:
                    balanced = False
                    #return balanced
                else:
                    print('second condition check')
                    temp = self.Pop() 
                    print('checking popped item ', temp)
                    if temp != i:
                        balanced = False
        if self.isEmpty() == True:
            balanced = False
        
        print('check boolean value ',balanced)
        return balanced
s = StackPython()
result = s.Solution('(())')
if result is True:
    print('balanced parenthesis')
else:
    print('unbalanced parenthesis')
                
                