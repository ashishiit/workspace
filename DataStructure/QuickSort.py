'''
Created on Jun 27, 2017

@author: S528358
'''
def Swap(a, leftPtr, rightPtr):
    temp = a[leftPtr]
    a[leftPtr] = a[rightPtr]
    a[rightPtr] = temp
def Partition(a, left, right):
    pivot = a[left]
    leftPtr = left + 1
    rightPtr = right
    while True:
        while a[leftPtr] <= pivot:
            leftPtr = leftPtr + 1
        while a[rightPtr] > pivot:
            rightPtr = rightPtr - 1
        if leftPtr > rightPtr:
            break
        else:
            Swap(a, leftPtr, rightPtr)
    Swap(a, left, rightPtr)
    return rightPtr
def Sort(a, leftPtr, rightPtr):
    if leftPtr < rightPtr:
        part = Partition(a, leftPtr, rightPtr)
        print(part)
        Sort(a, leftPtr, part-1)
        Sort(a, part+1, rightPtr)
a = [1, 3, 9, 8, 2, 7, 5]
Sort(a, 0, len(a)-1)
print(a)