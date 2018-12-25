'''
Created on Dec 16, 2017

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
            print(root.data,end = ' ')
            self.InOrder(root.right)
    def Display(self):
        self.InOrder(self.root)
    def Search(self,data):
        current = self.root
        while current.data is not data:
            if data > current.data:
                current = current.right
            else:
                current = current.left
            if current is None:
                return None
        return current
    def Delete(self,data):
        current = self.root
        while current.data is not data:
            parent = current
            if data > current.data:
                current = current.right
            else:
                current = current.left
            if current is None:
                return None
        
        if current.left is None and current.right is None:
            if current is self.root:
                self.root = None
            if current is parent.left:
                parent.left = None
            else:
                parent.right = None
        elif current.left is None:
            if current is self.root:
                self.root = current.right
            if current is parent.left:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if current is self.root:
                self.root = current.left
            if current is parent.right:
                parent.right = current.left
            else:
                parent.left = current.left
        
        elif current.left is not None and current.right is not None:
            successor = self.getSuccessor(self.current)
            if current is self.root:
                self.root = successor
            elif current == parent.right:
                parent.right = successor
            else:
                parent.left = successor
            successor.left = current.left
        
    def getSuccessor(self,delNode):
        current = delNode.right
        SuccessorParent = delNode
        Successor = delNode
        while current is not None:
            SuccessorParent = Successor
            Successor = current
            current = current.left
        if Successor != delNode.right:           
                Successor.right = delNode.right
                SuccessorParent.left = Successor.right
        return Successor
t = Tree()
t.Insert(20)
t.Insert(30)
t.Insert(40)
t.Insert(45)
t.Insert(50)
# t.Insert(45)
t.Insert(60)
t.Insert(47)
t.Insert(55)
t.Display()
print()
search = t.Search(50)
if search is None:
    print('element not found')
else:
    print('hurray!! element found')
t.Delete(30)
t.Display()