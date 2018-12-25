'''
Created on May 25, 2017

@author: S528358
'''
class Queue:
    def __init__(self):
        self.a = []
    def Enqueue(self,item):
        self.a.insert(0, item)
    def Dequeue(self):
        return self.a.pop()
    def Display(self):
        print(self.a)
    def IsEmpty(self):
        return self.a == []
    def Size(self):
        return len(self.a)
q = Queue()
q.Enqueue(8)
q.Enqueue(4)
q.Enqueue(89)
q.Display()
q.Dequeue()
q.Display()