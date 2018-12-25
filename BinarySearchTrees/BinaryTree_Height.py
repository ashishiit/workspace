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
        NewNode = Node(1)
        if self.root is None:
            self.root = NewNode
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.right = Node(4)
        self.root.right.left = Node(2)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end=' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Height(self,root):
        if root is None:
            return 0
        else:
            left_tree = self.Height(root.left)
            right_tree = self.Height(root.right)
            if left_tree > right_tree:
                return left_tree + 1
            else:
                return right_tree + 1
        
t = Tree()
t.Insert()
t.Display()
print('\nheight of tree = ', t.Height(t.root))