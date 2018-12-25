'''
Created on Dec 18, 2017

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
    def checkHeight(self,root):
        if root is None:
            return 0
        else:
            return max(self.checkHeight(root.left),self.checkHeight(root.right))+1
    def Balance(self,root):
        if root is None:
            return True
        else:
            return abs(self.checkHeight(root.left)-self.checkHeight(root.right))<=1 and self.Balance(root.left) and self.Balance(root.right)
#             return True
        return False
    def CheckBalance(self):
        return self.Balance(self.root)
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
t.Insert(25)
# t.Insert(35)
# t.Insert(32)
# t.Insert(38)
# t.Display()
result = t.CheckBalance()
if result is True:
    print('tree is height balanced')
else:
    print('not height balanced')