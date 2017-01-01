'''
Created on Oct 22, 2016

@author: s528358
'''
class Balanced:
    def __init__(self):
        self.a = []
    def Push(self,item):
        self.a.append(item)
    def Peek(self):
        return self.a[len(self.a)-1]
    def Pop(self):
        return self.a.pop()
    def IsEmpty(self):
        return self.a == []
    def Solution(self,s):
        balanced = True
        for i in s:
            if i=='(' or i=='{' or i=='[':
#                 print('pushed = %s'%i)
                self.Push(i)
            elif i==')' or i=='}' or i==']':
#                 print('first else')
                if self.IsEmpty():
#                     print('first else check')
                    balanced = False
                    break
                else:
                    test = self.Pop()
#                     print('popped = %s'%test)
                    if (i==')'and test!='(') or (i=='}' and test!='{') or (i==']' and test!='['):
#                         print('second else')
                        balanced = False
                        break
        if self.IsEmpty() == True and balanced == True:
#             print('check emptiness = %s'%self.IsEmpty())
#             print('balance check = %s'%balanced)
            print('symbols balanced')
        else:
#             print('check emptiness = %s'%self.IsEmpty())
#             print('balance check = %s'%balanced)
            print('Symbols not Balanced')
b = Balanced()
b.Solution('[((({(67)})))]')
            
        