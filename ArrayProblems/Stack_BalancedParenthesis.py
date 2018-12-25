'''
Created on Aug 17, 2018

@author: S528358
'''
class StackX:
    def __init__(self):
        self.a = []
    def Push(self,item):
        self.a.append(item)
    def Pop(self):
        return self.a.pop()
    def isEmpty(self):
        return self.a == []
    def Solution(self,s):
        isBalanced = True
        for i in s:
            if i=='(' or i=='{' or i=='[':
                self.Push(i)
            else:                
                if self.isEmpty():
                    
                    isBalanced = False
                    break
                else:
                    temp = self.Pop()
                    
                    if (i==')'and temp!='(') or (i=='}'and temp!='{') or (i==']'and temp!='['):
                        isBalanced = False
                        break
        
        if self.isEmpty() and isBalanced:
            return True
        else:
            return False
s = StackX()
result = s.Solution('(((((()')
print(result)