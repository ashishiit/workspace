'''
Created on Sep 22, 2017

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
            print(root.data, end = ' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Size(self,root):
        if root is None:
            return 0
        left_tree = self.Size(root.left)
        right_tree = self.Size(root.right)
        return left_tree+right_tree+1
    def Solution(self):
        print('size of tree = ',self.Size(self.root))
t = Tree()
t.Insert(20)
t.Insert(15)
t.Insert(30)
t.Insert(10)
t.Insert(16)
t.Insert(25)
t.Insert(40)
t.Insert(35)
t.Insert(50)
t.Insert(32)
t.Insert(36)
t.Insert(60)
t.Display()
print()
t.Solution()