'''
Created on Jun 17, 2018

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
        def Serial(root):
            if root is None:
                temp.append(None)
                return None
            else:                          
               
                temp.append(root.data)           
                self.InOrder(root.left)                               
                self.InOrder(root.right)
                
        
        Serial(root)
        return temp
t = Tree()
t.Insert(20)
t.Insert(10)
t.Insert(30)
temp = []
print(t.InOrder(t.root))
# print(temp)