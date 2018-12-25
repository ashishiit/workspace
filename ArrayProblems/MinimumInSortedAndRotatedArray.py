'''
Created on May 29, 2018

@author: s528358
'''
def Solution(a):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = (left+right)//2
        if a[mid-1] > a[mid]:
            return a[mid]
        elif a[mid] < a[len(a)-1]:
            right = mid-1
        else:
            left = mid + 1
        
a = [6, 7, 1, 2, 3, 4, 5]
print('minimum number is = ', Solution(a))
