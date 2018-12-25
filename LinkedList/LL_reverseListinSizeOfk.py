'''
Created on Dec 23, 2018

@author: S528358
'''
class Link:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class List:
    def __init__(self):
        self.first = None
        
    def Solution(self,head,k):
        