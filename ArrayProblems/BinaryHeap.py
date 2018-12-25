'''
Created on Oct 4, 2018

@author: s528358
'''
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0
    def Insert(self,item):
        self.heapList.append(item)
        self.heapSize = self.heapSize + 1
        self.trickleUp(self.heapSize)
    def trickleUp(self,index):
        parent = (index-1)//2
        while parent>0 and self.heapList[index]<self.heapList[parent]:
            temp = self.heapList[index]
            self.heapList[index] = self.heapList[parent]
            self.heapList[parent] = temp
            
            index = parent
            parent = (index-1)//2
    def Display(self):
        print(self.heapList[1:])
    def remMin(self):
        rem = self.heapList[1]
        print('minimum element = ',rem)
        self.heapList[1] = self.heapList[self.heapSize-1]
        self.heapSize = self.heapSize - 1
        self.trickleDown(1)
    def trickleDown(self,index):
        while index < self.heapSize:
            leftChild = 2*index
            rightChild = 2*index + 1
            if self.heapList[leftChild] < self.heapList[rightChild]:
                mc = leftChild
            else:
                mc = rightChild
            temp = self.heapList[index]
            self.heapList[index] = self.heapList[mc]
            self.heapList[mc] = temp
            
            index = mc
b = BinHeap()
b.Insert(5)
b.Insert(9)
b.Insert(11)
b.Insert(14)
b.Insert(18)
b.Insert(19)
b.Insert(21)
b.Insert(33)
b.Insert(17)
b.Insert(27)
b.Display()
b.remMin()
b.Display()