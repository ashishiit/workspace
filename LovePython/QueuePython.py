'''
Created on Oct 20, 2016

@author: S528358
'''
class QueuePython:
    def __init__(self):
        self.a = []
    def Push(self, item):
        self.a.append(item)
    def Peek(self):
        return self.a[0]
    def Remove(self):
        self.a.pop(0)
    def Display(self):
        print(self.a)
s = QueuePython()
s.Push(4)
s.Push(5)
s.Push(6)
s.Push(7)
s.Push(8)
s.Display()
print('first element of Queue = %d'%s.Peek())
s.Remove()
print('first element of Queue = %d'%s.Peek())  
s.Display()   