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
            print(root.data, end=' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Solution(self):
        q = []
        q.append(self.root)
        while True:
            length = len(q)
            if length == 0:
                break
            while length > 0:
                temp = q.pop(0)
                print(temp.data,end = ' ')
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                length = length - 1
            print('\n')
        
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