'''
Created on Oct 14, 2017

@author: S528358
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
class Tree:
    def __init__(self):
        self.root = None
            
    def Insert(self,data):
        self.Update(data)
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
        