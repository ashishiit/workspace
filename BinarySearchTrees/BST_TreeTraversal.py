'''
Created on Aug 17, 2017

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
    def Insert(self,value):
        NewNode = Node(value)
        if self.root is None:
            self.root = NewNode
        else:
            current = self.root            
            while True:
                parent = current
                if value > current.data:
                    current = current.right
                    if current is None:
                        parent.right = NewNode
                        return
                else:
                    current = current.left
                    if current is None:
                        parent.left = NewNode
                        return
    def InOrder(self,root,result=[]):
        if root is None:
            result.append(None)
        else:
            print(root.data)
            result.append(root.data)
            self.InOrder(root.left)            
            self.InOrder(root.right)
#         ret = ['']
        print(result)
    def Display(self):
        result = []
        self.InOrder(self.root,result)
        print(result)
    ret = ['']
t = Tree()
t.Insert(25)
t.Insert(15)
t.Insert(50)
t.Insert(10)
t.Insert(22)
t.Insert(35)
t.Insert(70)
t.Insert(4)
t.Insert(12)
t.Insert(18)
t.Insert(24)
t.Insert(31)
t.Insert(44)
t.Insert(66)
t.Insert(90)
t.Display()
