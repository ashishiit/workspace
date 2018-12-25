'''
Created on Sep 23, 2017

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
            return None
        else:
            self.InOrder(root.left)
            print(root.data, end=' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Height(self,root):
        if root is None:
            return 0
        left_tree = self.Height(root.left)
        right_tree = self.Height(root.right)
        if left_tree > right_tree:
            return left_tree+1
        else:
            return right_tree+1
    def Solution(self):
        print('height of the tree = ',self.Height(self.root))
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
t.Insert(40)
t.Insert(35)
t.Insert(50)
t.Display()
print()
t.Solution()