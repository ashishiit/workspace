'''
Created on Jun 23, 2018

@author: s528358
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
        
    def Display(self):
        self.InOrder(self.root)
        
    def InOrder(self,root):
        if root is None:
            return
        self.InOrder(root.left)
        print(root.data, end=' ')
        self.InOrder(root.right)
        
    def getLevel(self,target):
        return self.Solution(self.root,target,1)
    
    def Solution(self,root,target,level):
        if root is None:
            return 0
        elif root.data == target:
            return level        
        downlevel = self.Solution(root.left, target, level + 1)
        if downlevel != 0:
            return downlevel
  
        downlevel = self.Solution(root.right, target, level + 1)
#         return downlevel
t = Tree()
t.Display()
print('level of given node = ',t.getLevel(6))
    
    