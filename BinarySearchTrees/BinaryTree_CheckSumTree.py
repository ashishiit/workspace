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
        if self.root == None:
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
            return None
        else:
            self.InOrder(root.left)
            print(root.data, end=' ')
            self.InOrder(root.right)
            
    def CheckSum(self):
        return self.Solution(self.root)
        
    def Solution(self,root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True    

        left_sum = self.Sum(root.left)
        right_sum = self.Sum(root.right)
#         print('node sum = ', left_sum+right_sum)
        return root.data==left_sum+right_sum and self.Solution(root.left) and self.Solution(root.right)
    
    def Sum(self,root):
        if root is None:
            return 0
        return self.Sum(root.left)+root.data+self.Sum(root.right)
t = Tree()
t.Display()
result = t.CheckSum()
if result is True:
    print('is Sum Tree')
else:
    print('is NOT Sum Tree')