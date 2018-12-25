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
    def Count_Size(self,root):
        if root is None:
            return 0
        return self.Count_Size(root.left)+self.Count_Size(root.right)+1
    def Size(self):
        return self.Count_Size(self.root)
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
t.Insert(25)
t.Insert(35)
t.Insert(32)
t.Display()
print()
print('size of tree is = ',t.Size())