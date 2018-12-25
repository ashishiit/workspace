'''
Created on Jun 19, 2018

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
        NewNode = Node(1)
        if self.root is None:
            self.root = NewNode
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.right = Node(4)
        self.root.right.left = Node(2)
    
    def Height(self,root):
        if root is None:
            return 0
        else:
            if self.Height(root.left) > self.Height(root.right):
                return self.Height(root.left)+1
            else:
                return self.Height(root.right)+1
                
    def PrintNodes(self, root, level, temp):
        if root is None:
            temp.append(None)
            return None
        elif level == 1:
            temp.append(root.data)
        else:
            self.PrintNodes(root.left, level-1,temp)
            self.PrintNodes(root.right, level-1, temp)
        return temp    
    def serialize_tree(self,root):
#         temp = []
        result = []
        h = self.Height(root)
        for i in range(1, h+1):
            temp = []
            self.PrintNodes(root,i,temp)
            result.append(temp)
        return result

t = Tree()
print(t.serialize_tree(t.root))   