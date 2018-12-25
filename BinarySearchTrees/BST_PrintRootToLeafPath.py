'''
Created on Dec 19, 2017

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
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end = ' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def PrintPath(self,root, temp):
#         print(root.data)
        if root is None:
            return None
        if root is not None:
            temp.append(root.data)
        if root.left is None and root.right is None:
            print(temp)
            temp.pop()
#             print()
            temp = []        
        else:
            self.PrintPath(root.left, temp)
            self.PrintPath(root.right, temp)        
    def Solution(self):
        temp = []
        self.PrintPath(self.root, temp)
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
# t.Insert(25)
t.Insert(35)
# t.Insert(32)
t.Insert(38)
# t.Display()
t.Solution()