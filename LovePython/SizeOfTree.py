'''
Created on Dec 30, 2016

@author: S528358
'''
# from aifc import data
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Size:
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
        print('size of tree = ', self.Size_Solution(self.root))
    def Size_Solution(self,root):
        if root is None:
            return 0
        left = self.Size_Solution(root.left)
        right = self.Size_Solution(root.right)
        return left + right + 1
s = Size()
s.Insert(30)
s.Insert(40)
s.Insert(10)
s.Solution()