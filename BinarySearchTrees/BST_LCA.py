'''
Created on Aug 14, 2017

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
    def Insert(self, data):
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
    def InOrder(self,root):
        if root is None:
            return None
        else:
            self.InOrder(root.left)
            print(root.data)
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Solution(self,root, v1, v2):
        if root is None:
            return None
        elif root.data>v1 and root.data>v2:
            return self.Solution(root.left, v1, v2)
        elif root.data<v1 and root.data<v2:
            return self.Solution(root.right, v1, v2)
        return root.data
    def LCA(self,v1, v2):
#         print(self.root.data)
        return self.Solution(self.root, v1, v2)
t = Tree()
t.Insert(4)
t.Insert(2)
t.Insert(7)
t.Insert(1)
t.Insert(3)
t.Insert(6)
t.Display()
print('lca = ',t.LCA(967,89))