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
        answer = self.Close(self.root,k)
        print('closest element = %d'%answer)
    def Close(self,root,k):
#         if root.data == k:
#             return root.data
        temp = []
        while root.left is not None and root.right is not None:
            if root.data == k:
                return root.data
            if k > root.data:
                temp.append([k-root.data,root.data])
                root = root.right                
            else:
                temp.append([root.data-k,root.data])
                root = root.left               
            
        temp.sort()  
        return temp[0][1]  
#         print('closest element = %d'%temp[0][1])
t = Tree()
t.Insert(9)
t.Insert(4)
t.Insert(17)
t.Insert(3)
t.Insert(6)
t.Insert(12)
t.Insert(5)
t.Insert(7)
t.Insert(20)
t.Display()
t.Solution(12)