'''
Created on Jan 3, 2017

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
            return
        else:
            self.InOrder(root.left)
            print(root.data,end = ' ')
            self.InOrder(root.right)
    def Solution(self,root):
        if root is None:
            return
        self.Solution(root.left)
        self.Solution(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
t = Tree()
t.Insert(50)
t.Insert(10)
t.Insert(60)
t.Display()
t.Solution(t.root)
print()
t.Display()
        