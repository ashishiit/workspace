'''
Created on Jun 16, 2018

@author: S528358
'''
def Solution(a):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = (left+right)//2
        if a[mid] < a[mid-1]:
            return mid
        elif a[mid] > a[right]:
            left = mid + 1
        elif a[mid] < a[right]:
            right = mid - 1
a = [7, 9, 11, 12, 5]
print(Solution(a))