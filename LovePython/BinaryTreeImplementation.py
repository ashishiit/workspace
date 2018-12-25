'''
Created on Jan 13, 2017

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
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return None
        else:
            self.InOrder(root.left)
            print(root.data, end = ' ')
            self.InOrder(root.right)
t = Tree()
t.root = Node(1)
t.root.right = Node(1)
t.root.left = Node(None)
t.Display()