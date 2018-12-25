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
            return
        else:
            self.InOrder(root.left)
            print(root.data,end = ' ')
            self.InOrder(root.right)
    def Validate(self):
        self.previous = None
        return self.isValidate(self.root)
    def isValidate(self,root):
        if root is None:
            return
        self.isValidate(root.left)
        if self.previous is not None and self.previous.data>=root.data:
            return False
        self.previous = root
        self.isValidate(root.right)
        return True
t = Tree()
t.root = Node(1)
t.root.right = Node(3)
t.root.right.left = Node(2)
t.Display()
print(t.Validate())