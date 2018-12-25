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
        self.InOrder(self.root)
        
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data,end=' ')
            self.InOrder(root.right)
            
    def Nth(self,n):
        count = 0
        return self.Solution(self.root, n, count)
        
    def Solution(self,root, n,count):        
        if root is None:
            return
        print('node track = ', root.data)
#         else:
        self.Solution(root.left, n, count)        
        count = count + 1
        print('\ncount = ',count)
        if count == n-1:
            print('n =',n)
            return "aww"
        self.Solution(root.right, n, count)
        
t = Tree()
t.Display()
print()
print('nth node = ',t.Nth(3))