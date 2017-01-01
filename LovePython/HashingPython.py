'''
Created on Oct 29, 2016

@author: s528358
'''
class BasicHashing:
    def __init__(self):
        self.size = 12
        self.slots = [None]*self.size
    def hashFunction(self,key,size):
        return key%size
    def Insert(self,key):
        hashValue = self.hashFunction(key,self.size)
#         print(hashValue)
        while self.slots[hashValue] is not None and self.slots[hashValue] is not 'Del':
            hashValue = hashValue + 1
            hashValue = hashValue % self.size
        self.slots[hashValue] = key
    def Search(self,key):
        hashValue = self.hashFunction(key, self.size)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue] == key:
                return "item found"
            else:
                hashValue = hashValue + 1
                hashValue = hashValue % self.size
        return "Not Found"
    def Display(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(self.slots[i], end = ' ')
            else:
                print(" ",end = ' ')
    def Delete(self,key): 
        '''item needs to be deleted before searching'''       
        hashValue = self.hashFunction(key,self.size)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue] == key:
                self.slots[hashValue] = 'Del'
                return 'item deleted'
            else:
                hashValue = hashValue + 1
                hashValue = hashValue % self.size
        return 'item to be Deleted Not Found'
h = BasicHashing()
h.Insert(108)
h.Insert(13)
h.Insert(0)
h.Insert(113)
h.Insert(5)
h.Insert(6)
h.Insert(117)
h.Insert(47)
h.Display()
print("\n",h.Search(113))
print("\n",h.Delete(108))
h.Display()
print()
h.Insert(108)
h.Display()