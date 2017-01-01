'''
Created on Oct 26, 2016

@author: s528358
'''
# import string
class StackPython:
    def __init__(self):
        self.a = []
    def Push(self,item):
        self.a.append(item)
    def Pop(self):
        return self.a.pop()
    def Peek(self):
        return self.a[len(self.a)-1]
    def IsEmpty(self):
        return self.a == []
    def Solution(self, num):
        while num != 0:
            item = num % 2
#             print('item pushed = %d'%item)
            self.Push(item)
            num = num // 2
#         print(self.a)
#         print(self.a.reverse())
        self.a.reverse()
        print(self.a)
s = StackPython()
s.Solution(6)