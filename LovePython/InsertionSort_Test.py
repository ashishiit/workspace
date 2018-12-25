'''
Created on Feb 3, 2017

@author: s528358
'''
import unittest
from InsertionSort import Solution
a = [1, 10, -67, -2, 2]
class InsertSort_Test(unittest.TestCase):
    def test_InsertionSort(self):
        try:
            if Solution(a) != sorted(a):
                raise Exception('incorrect')
        except Exception as e:
            print(e)
                
        