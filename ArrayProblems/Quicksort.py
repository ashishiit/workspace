'''
Created on May 25, 2018

@author: s528358
'''
def QuickSort(a, left, right):
    if left < right:
       
        partition = partitionFunc(a,left,right)
        QuickSort(a,left,partition-1)
        QuickSort(a,partition+1, right)
    
def partitionFunc(a,left, right):
    pivot = a[right]
    leftPtr = left
    rightPtr = right-1
    
    while leftPtr < rightPtr:
        while a[leftPtr] < pivot:
            leftPtr = leftPtr + 1
        while a[rightPtr] > pivot:
            rightPtr = rightPtr - 1
        if leftPtr < rightPtr:
            Swap(a,leftPtr, rightPtr)
    Swap(a,leftPtr,right)
    print('pivot =', leftPtr)
    return leftPtr
def Swap(a, left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp    
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
QuickSort(a, 0, len(a)-1)
print(a)