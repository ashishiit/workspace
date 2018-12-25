'''
Created on Jun 12, 2018

@author: S528358
'''
class StackX:
    def __init__(self,size):
        self.size = size
        self.a = [None]*size
        self.top1 = 0
        self.top2 = self.size - 1
        
    
    def Push1(self,item):
        if self.top1 < self.top2-1:
            self.a[self.top1] = item
            self.top1 = self.top1 + 1
        else:
            print('overflow')
            
    def Push2(self,item):
        if self.top1 < self.top2-1:
            self.a[self.top2] = item
            self.top2 = self.top2 - 1
        else:
            print('overflow')
            
    def Pop1(self):
        if self.top1 >= 0:
            temp = self.a[self.top1]
            self.top1 = self.top1 - 1
            return temp
        else:
            print('underflow')
            
    def Pop2(self):
        if self.top2 < self.size:
            temp = self.a[self.top2]
            self.top2 = self.top2 + 1
            return temp
        else:
            print('underflow')

ts = StackX(5)
ts.Push1(5)
ts.Push2(10)
ts.Push2(15)
ts.Push1(11)
ts.Push2(7)
print("Popped element from stack1 is " ,ts.Pop1())
ts.Push2(40)
print("Popped element from stack2 is ", ts.Pop2())
            