'''
Created on Jan 14, 2017

@author: S528358
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def SortedArray(self,a):
        self.root = self.Convert(a, 0, len(a))
#         print(self.root.data)
    def Convert(self, a, begin, end):
        if begin >= end:
            return None
#         mid = begin+(end-begin)//2
        mid = (begin+end)//2
        root = Node(a[mid])
        root.left = self.Convert(a, begin, mid)
        root.right = self.Convert(a, mid+1, end)
        return root
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end = ' ')
            self.InOrder(root.right)
a = [1,2,3,4,5,6,7]
t = Tree()
t.SortedArray(a)
t.Display()