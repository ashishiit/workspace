'''
Created on Jan 12, 2017

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
        else:
            current = self.root
            while True:
                parent = current
                if data > current.data:
                    current = current.right
                    if current is None:
                        parent.right = NewNode
                        return
                else:
                    current = current.left
                    if current is None:
                        parent.left = NewNode
                        return
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return None
        else:
            self.InOrder(root.left)
            print(root.data,end = ' ')
            self.InOrder(root.right)
    def CountLeftSubTree(self,root):
        if root is None:
            return None
        else:
            self.CountLeftSubTree(root.left)
            print('root%d and left%d'%(root.data, self.Count(root.left)))
            self.CountLeftSubTree(root.right)
    def Count(self,root):
        if root is None:
            return 0
        left_tree = self.Count(root.left)
        right_tree = self.Count(root.right)
        return left_tree + right_tree + 1
    
t = Tree()
t.Insert(20)
t.Insert(8)
t.Insert(22)
t.Insert(4)
t.Insert(12)
t.Insert(10)
t.Insert(14)
# t.Display()
t.CountLeftSubTree(t.root)