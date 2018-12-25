'''
Created on Dec 19, 2017

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
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end = ' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Count_LeafNodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.Count_LeafNodes(root.left)+self.Count_LeafNodes(root.right)
    def Solution(self):
        return self.Count_LeafNodes(self.root)
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
t.Insert(25)
t.Insert(35)
t.Display()
print()
print('# of leaf nodes = ',t.Solution())