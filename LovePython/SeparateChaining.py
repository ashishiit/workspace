'''
Created on Dec 24, 2016

@author: S528358
'''
class Link:
    def __init__(self,data = None):
        self.next = None
        self.data = data
class SeparateChain:
    def __init__(self):
        self.first = None
        self.last = None
    def Insert(self,data):
        NewLink = Link(data)
        if self.last is None:
            self.first = NewLink
        else:
            self.last.next = NewLink
        self.last = NewLink
    def Display(self):
        current = self.first
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
class SeparateChaining:
    '''create multiple objects'''
    def __init__(self):
#         a[index] = Link()
        self.a = [None] * 12
        for i in range(12):
            self.a[i] = SeparateChain()
#         l = Link(a)
#         for i in range(12):
            
    def hashFunction(self,key, size):
        return key%size
    def Insert(self,key):
        hashVal = self.hashFunction(key,size = 12)
#         print(hashVal)
        self.a[hashVal].Insert(key)
    def Display(self):
        for i in range(12):
            print(self.a[i])
# h.Insert(108)
# h.Insert(13)
# h.Insert(0)
# h.Insert(113)
# h.Insert(5)
# h.Insert(6)
# h.Insert(117)
# h.Insert(47)
test = SeparateChaining()
test.Insert(108)
test.Insert(13)