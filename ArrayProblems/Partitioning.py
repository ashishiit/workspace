'''
Created on May 24, 2018

@author: s528358
'''
def Swap(a, left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
def Solution(a):
    pivot = a[len(a)-1]
    left = 0
    right = len(a)-2
    while left < right:
        while a[left]<pivot:
            left = left + 1
        while a[right]>pivot:
            right = right - 1
        if left < right:
            Swap(a, left, right)
    Swap(a,left,len(a)-1)
    print(a)
    print('partition = ',left)
a=[149, 192, 47, 152, 159, 195, 61, 66, 17, 167, 118, 64, 27, 80, 30, 105]
Solution(a)