'''
Created on Sep 21, 2018

@author: S528358
'''
def ArraySplitAddEnd(a,k):
    n = len(a)
    Reverse(a,0,n-1)
    Reverse(a,0,n-1-k)
    Reverse(a,n-k,n-1)
    print(a)
def Reverse(a,left,right):
    while left < right:
        temp = a[right]
        a[right] = a[left]
        a[left] = temp
        left = left + 1
        right = right - 1
a = [12, 10, 5, 6, 52, 36]
k = 2
ArraySplitAddEnd(a,k)