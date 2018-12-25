'''
Created on Jun 22, 2018

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
        NewNode = Node(26)
        if self.root is None:
            self.root = NewNode
        self.root.left = Node(10)
        self.root.left.left = Node(4)
        self.root.left.right = Node(6)
        self.root.right = Node(3)
        self.root.right.right = Node(3)
    
    def InOrder(self,root):
        if root is None:
            return None
        else:
            self.InOrder(root.left)
            print(root.data,end=' ')
            self.InOrder(root.right)    
    def Display(self):
        self.InOrder(self.root)
        
    def Solution(self,root):
        if root is None:
            return 0
        else:
            return self.Solution(root.left)+root.data+self.Solution(root.right)
        
    def SumNodes(self):
#         result = 0
        result= self.Solution(self.root)
        print('result = ',result)
t = Tree()
t.Display()
t.SumNodes()