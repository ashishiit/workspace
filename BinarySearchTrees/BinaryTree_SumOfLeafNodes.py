'''
Created on Aug 15, 2018

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
    def Insert(self):
        NewNode = Node(1)
        self.root = NewNode
        self.root.left = Node(2)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right = Node(3)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.right.left.right = Node(8)
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data,end=' ')
            self.InOrder(root.right)
    def Solution(self):
        result = self.CountLeaf(self.root)
        print('sum of leaf nodes = ',result)
    def CountLeaf(self,root):
        if root is None:
            return 0
        lefttree = self.CountLeaf(root.left)
        righttree = self.CountLeaf(root.right)
        if lefttree==0 and righttree==0:
            return lefttree + righttree + root.data
        return self.CountLeaf(root.left)+self.CountLeaf(root.right)
t = Tree()
t.Insert()
t.Display()
print()
t.Solution()