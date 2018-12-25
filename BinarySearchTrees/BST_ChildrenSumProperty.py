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
    def Check_Sum(self,root):
        if root is None or (root.left is None and root.right is None):
            return True
        if root.left is not None:
            left_data = root.left.data
        else:
            left_data = 0
        if root.right is not None:
            right_data = root.right.data
        else:
            right_data = 0
        return root.data==left_data+right_data and self.Check_Sum(root.left) and self.Check_Sum(root.right)
    def Solution_Check_Sum(self):
        return self.Check_Sum(self.root)
t = Tree()
t.Insert(20)
t.Insert(22)
t.Insert(-2)
t.Display()
result = t.Solution_Check_Sum()
print()
if result is True:
    print('children sum property satisfied')
else:
    print('CHILDREN SUM PROPERTY NOT SATISFIED')