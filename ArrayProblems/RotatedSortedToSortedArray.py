'''
Created on Sep 22, 2018

@author: S528358
'''
def Reverse(a, left, right):
    while left < right:
        temp = a[right]
        a[right] = a[left]
        a[left] = temp
        left = left + 1
        right = right - 1
def Solution(a):
    n = len(a)
    temp = 0
    for i in range(1,n):
        if a[i] < a[i-1]:
            temp = i
            break
    Reverse(a, 0, temp-1)
    Reverse(a, temp,n-1)
    Reverse(a, 0,n-1)
    print(a)
a = [3,4,1,2]
Solution(a)