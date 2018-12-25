'''
Created on Dec 17, 2017

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
    def Sum(self,root,n):
        if root is None:
            return False
        else:
            if root.data==n and root.left is None and root.right is None:
                return True
            return self.Sum(root.left,n-root.data) or self.Sum(root.right, n-root.data)
    def Calculate_Sum(self,n):
        return self.Sum(self.root, n)
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
# print(t.root.data)
# t.Display()
result = t.Calculate_Sum(20)
print()
# print(result)
if result == True:
    print('root to leaf sum exist')
else:
    print('root to leaf SUM NOT EXIST')