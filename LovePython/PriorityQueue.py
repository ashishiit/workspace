'''
Created on Dec 27, 2016

@author: S528358
'''
class Priority:
    def __init__(self):
        self.a = []
        self.size = None
    def Solution(self,data):
        print('fist condition')
        print(self.size)
        if self.size == 0:
            self.a.append(data)
        else:
            print('check condition')
            i = len(self.a)
            while i-1 >= 0:
                if data > self.a[i-1]:
                    self.a[i] = self.a[i-1]
                else:
                    break
            self.a[i+1] = data
    def Display(self):
        for i in self.a:
            print(i, end = ' ')
test = Priority()
test.Solution(67)
test.Solution(-45)
test.Solution(0)
test.Solution(789)
test.Display()