'''
Created on Dec 31, 2016

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
    def Solution(self):
        print('height of tree ', self.height(self.root))
    def height(self,root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left > right:
            return left+1
        else:
            return right+1
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return
        self.InOrder(root.left)
        print(root.data, end= ' ')
        self.InOrder(root.right)
    
t = Tree()
t.Insert(10)
t.Insert(20)
t.Insert(30)
t.Insert(25)
t.Insert(40)
t.Display()
t.Solution()