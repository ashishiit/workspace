'''
Created on Jan 8, 2017

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
    def LCA(self,root,node1, node2):
        if root is None:
            return None
        if root.data>node1 and root.data>node2:
            return self.LCA(root.left,node1,node2)
        if root.data<node1 and root.data<node2:
            return self.LCA(root.right,node1,node2)
        return root.data    
t = Tree()
t.Insert(10)
t.Insert(-1)
t.Insert(30)
t.Insert(8)
t.Insert(25)
t.Insert(60)
t.Insert(6)
t.Insert(9)
t.Insert(28)
t.Insert(78)
t.Display()
print('lca = %d'%t.LCA(t.root,28,30))