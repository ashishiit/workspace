'''
Created on Jun 24, 2018

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
        temp = []
        self.InOrder(self.root, temp)
        print(temp)
        
    def InOrder(self,root,temp):
        if root is None:
            return
        else:
            self.InOrder(root.left,temp)
            temp.append(root.data)
            self.InOrder(root.right, temp)
            
    def Solution(self):
        h = self.Height(self.root)
#         result = []
        for i in range(h,0,-1):
            self.PrintNodes(self.root,i)
            
    def Height(self,root):
        if root is None:
            return 0
        elif self.Height(root.left) > self.Height(root.right):
            return self.Height(root.left)+1
        else:
            return self.Height(root.right)+1
    
    def PrintNodes(self,root,level):
        if root is None:
            return
        if level == 1:
            print(root.data,end=' ')
        else:
            self.PrintNodes(root.left, level-1)
            self.PrintNodes(root.right, level-1)

t = Tree()
t.Display()
t.Solution()            