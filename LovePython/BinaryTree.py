'''
Created on Jan 9, 2017

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
            self.Add(NewNode,self.root)
    def Add(self,NewNode, root):
        if NewNode.data < root.data:
            if root.left is None:
                root.left = NewNode
            else:
                self.Add(NewNode,root.left)
        else:
            if root.right is None:
                root.right = NewNode
            else:
                self.Add(NewNode,root.right)
    def Display(self):
        self.InOrder(self.root)
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, end=' ')
            self.InOrder(root.right)
    def LCA(self,root,node1, node2):
        if root is None:
            return None
        if root.data==node1 or root.data==node2:
            return root
        left_tree = self.LCA(root.left,node1,node2)
        right_tree = self.LCA(root.right,node1,node2)
        if left_tree is not None and right_tree is not None:
            return root
        if left_tree is not None:
            return left_tree
        else:
            return right_tree
        

t = Tree()
t.Insert(1)
t.Insert(2)
t.Insert(3)
# t.Insert(8)
# t.Insert(2)
t.Display()
num = t.LCA(t.root,2,8)
print("lca = %d\n"%num.data)