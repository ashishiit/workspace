'''
Created on Jun 19, 2018

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
    def Insert(self):
        NewNode = Node(5)
        if self.root is None:
            self.root = NewNode
        
        self.root.left = Node(2)
        self.root.left.left = Node(-2)
        self.root.left.right = Node(4)
        self.root.right = Node(3)
        self.root.right.left = Node(2)
        self.root.right.right = Node(1)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end = ' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Solution(self,root,count, n):
        if root is None:
            return       
#             count = count + 1
        count = count + 1
        self.Solution(root.left, count, n)
        print('\ncount = ', count)
        print('Nth node = ',root.data)
#         count = count + 1
#         if count == n:
#             print('\ncount = ', count)
#             print('Nth node = ',root.data)
        count = count + 1
        self.Solution(root.right, count, n)

    def Nth(self,n):
        count = 1
        self.Solution(self.root,count, n)
#         print(count)
        print('main = ',count)
t = Tree()
t.Insert()
t.Display()
t.Nth(3)