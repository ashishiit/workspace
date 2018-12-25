import unittest, random
from Main_Solution import Insertion_Sort, QuickSort_Sort,Builtin_Sort, Select_Algo
L = random.sample(range(1,101),100)
# print(L)
k = int(input('k ='))
'''sorted() returns sorted list'''
class Sort_test(unittest.TestCase):
    def test_InsertionSort(self):
        '''Insertion Sort'''
        a = L
        self.assertEqual(Insertion_Sort(a)[k], Select_Algo(a, 0, len(a)-1, k), msg = None)        
    def test_QuickSort(self):
        '''Quick Sort'''
        a = L
        self.assertEqual(QuickSort_Sort(a,0,len(a)-1)[k], Select_Algo(a, 0, len(a)-1, k), msg = None)
    def test_Builtin(self):
        '''Builtin Sort'''
        a = L
        self.assertEqual(Builtin_Sort(a)[k], Select_Algo(a, 0, len(a)-1, k), msg = None)