'''
Created on Jun 18, 2018

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
    def Insert(self,data):
        NewNode = Node(data)
        if self.root is None:
            self.root = NewNode
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.right = Node(4)
        self.root.right.left = Node(2)
    def InOrder(self,root,temp):
        if root is None:
            return None
        else:
            self.InOrder(root.left,temp)
            temp.append(root.data)
            self.InOrder(root.right,temp)
    def Display(self):
        temp = []
        self.InOrder(self.root,temp)
        print(temp)
t = Tree()
t.Insert(1)
t.Insert(2)
t.Insert(3)
t.Insert(4)
t.Insert(5)
t.Display()