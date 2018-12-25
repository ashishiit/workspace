'''
Created on Jan 15, 2017

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
        self.InOrder(root.left)
        print(root.data, end = ' ')
        self.InOrder(root.right)
    def Solution(self, root1, root2):
        total = 10
        self.root1_data = []
        self.root2_data = []
        self.FirstTree(self.root1_data, root1)
        self.SecondTree(self.root2_data, root2)
        print('first tree = ',self.root1_data)
        print('second tree =',self.root2_data)
        left = 0
        right = len(self.root2_data) - 1
        while left<len(self.root1_data) and right>=0:
            if self.root1_data[left]+self.root2_data[right] < total:
                left = left + 1
            elif self.root1_data[left]+self.root2_data[right] > total:
                right = right - 1
            elif self.root1_data[left]+self.root2_data[right] == total:
                print('%d and %d'%(self.root1_data[left], self.root2_data[right]))
                left = left + 1
                right = right - 1
    def FirstTree(self,root1_data, root1):
        if root1 is None:
            return
        else:
            self.FirstTree(root1_data, root1.left)
            root1_data.append(root1.data)
            self.FirstTree(root1_data, root1.right)
    def SecondTree(self,root2_data, root2):
        if root2 is None:
            return
        else:
            self.SecondTree(root2_data, root2.left)
            root2_data.append(root2.data)
            self.SecondTree(root2_data, root2.right)
        
t1 = Tree()
t2 = Tree()
t1.Insert(8)
t1.Insert(3)
t1.Insert(10)
t1.Insert(1)
t1.Insert(6)
t1.Insert(14)
t1.Insert(5)
t1.Insert(7)
t1.Insert(13)
t2.Insert(5)
t2.Insert(2)
t2.Insert(18)
t2.Insert(1)
t2.Insert(3)
t2.Insert(4)
t1.Display()
print()
t2.Display()
print()
t = Tree()
t.Solution(t1.root, t2.root)