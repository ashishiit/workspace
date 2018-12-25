'''
Created on Dec 20, 2018

@author: S528358
'''
import unittest
def Div(x):
    return x/0
    
class MyTest(unittest.TestCase):
    def Test(self):
        try:
            self.Div(5)
        except Exception as e:
            print(e)