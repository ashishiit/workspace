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
            print(root.data,end=' ')
            self.InOrder(root.right)
    def Solution(self,node1,node2):
        self.BSTsolution(self.root, node1, node2)
    def BSTsolution(self,root, node1, node2):
        if root is None:
            return None
        else:
            self.BSTsolution(root.left, node1, node2)
            if root.data>=node1 and root.data<=node2:
                print(root.data, end=' ')
            self.BSTsolution(root.right, node1, node2)
    
t = Tree()
t.Insert(20)
t.Insert(8)
t.Insert(22)
t.Insert(4)
t.Insert(12)
# t.Display()
t.BSTsolution(t.root, 10, 22)