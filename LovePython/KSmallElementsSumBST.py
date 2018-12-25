'''
Created on Jan 14, 2017

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
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end = ' ')
            self.InOrder(root.right)
    def Solution(self,k):
        self.count = 0
        self.sum = 0
        answer = self.Small(k,self.root)
        print('sum of k small elements = ',answer)
    def Small(self,k,root):
#         print(self.count)
        if k <= 0:
            return 'wrong input'
        if self.count > k:
            return
        if root is None:
            return
        else:
            self.Small(k,root.left)
            if self.count < k:
                self.sum = self.sum + root.data
                self.count = self.count + 1
            self.Small(k,root.right)
        return self.sum
t = Tree()
t.Insert(8)
t.Insert(7)
t.Insert(10)
t.Insert(2)
t.Insert(9)
t.Insert(13)
t.Display()
t.Solution(3)