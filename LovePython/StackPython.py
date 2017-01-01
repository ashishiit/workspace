'''
Created on Sep 30, 2016

@author: S528358
'''
class StackPython:
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
    def Display(self):
        print(self.a)
    def Size(self):
        return len(self.a)
s = StackPython()
s.Push(45)
s.Push('love')
s.Push('you')
s.Push(67)
s.Push(456)
s.Display()
print('size of the stack ',s.Size())
print('popped item', s.Pop())
s.Display()
print('size of the stack after 1 pop ', s.Size())
print('top item on the stack ', s.Peek())
print('is stack is empty?',s.isEmpty())
s.Pop()
s.Pop()
s.Pop()
s.Pop()
print('is stack is empty?',s.isEmpty())