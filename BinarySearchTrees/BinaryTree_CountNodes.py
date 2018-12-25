'''
Created on Jun 19, 2018

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
        NewNode = Node(5)
        if self.root is None:
            self.root = NewNode
        self.root.left = Node(2)
        self.root.left.left = Node(-2)
        self.root.left.right = Node(4)
        self.root.right = Node(3)
        self.root.right.left = Node(2)
        self.root.right.right = Node(1)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end=' ')
            self.InOrder(root.right)        
    def Display(self):
        self.InOrder(self.root) 
    def Solution(self,root):
        if root is None:
            return 0
        left_tree = self.Solution(root.left)
        right_tree = self.Solution(root.right)
        return left_tree + right_tree + 1
        return self.Solution(root.left)+self.Solution(root.right)
    def CountNodes(self):        
        return self.Solution(self.root)
t = Tree()
t.Insert()
t.Display()
print('\nnumber of nodes = ',t.CountNodes())