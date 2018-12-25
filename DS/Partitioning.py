'''
Created on Jul 2, 2017

@author: S528358
'''
def Swap(a, left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
def Partition_method3(a, left, right):
    pivot = a[0]
    left = left + 1
    while True:
        while a[left] < pivot:
            left = left + 1
        while a[right] > pivot:
            right = right - 1
        if left > right:
            break
        else:
            Swap(a, left, right)
    Swap(a,right,a.index(pivot))
    print(a)
def Partition_method2(a, left, right):
    pivot = a[right]
    right = right - 1
    while True:
        
        while a[left] < pivot:
            left = left + 1
        while a[right] > pivot:
            right = right - 1
        if left > right:
            break
        else:
            Swap(a, left, right)
    Swap(a,left,a.index(pivot))
    print(a)
def Partition_method1(a, left, right):
    pivot = 99
    while True:
        while a[left] < pivot:
            left = left + 1
        while a[right] > pivot:
            right = right - 1
        if left > right:
            break
        else:
            Swap(a, left, right)
    print(a)    
a = [149, 192, 47, 152, 159, 195, 61, 66, 17, 167, 118, 64, 27, 80, 30, 105]
Partition_method1(a, 0, len(a)-1)
Partition_method2(a, 0, len(a)-1)
Partition_method3(a, 0, len(a)-1)