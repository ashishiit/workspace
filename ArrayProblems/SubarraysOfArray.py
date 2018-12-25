'''
Created on May 20, 2018

@author: S528358
'''
from functools import reduce
a = [1, 2, 3, 4]
for i in range(len(a)):
    for j in range(1,len(a)+1):
        if len(a[i:j]) != 0:
            print(a[i:j])
            nums_product = reduce( (lambda x, y: x * y), a[i:j])
            print(nums_product)
