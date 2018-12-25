'''
Created on Aug 3, 2018

@author: s528358
'''
def MergeSort(a):
    if len(a) == 1:
        return
    else:
        mid = len(a)//2
        leftArray = a[:mid]
        rightArray = a[mid:]
        MergeSort(leftArray)
        MergeSort(rightArray)
        Merge(a,leftArray,rightArray)
def Merge(a, leftArray, rightArray):
#     print(a)
    i = 0
    j = 0
    k = 0
    while i<len(leftArray) and j<len(rightArray):
        if leftArray[i] < rightArray[j]:
            a[k] = leftArray[i]
            i = i + 1
            k = k + 1
        elif rightArray[j] < leftArray[i]:
            a[k] = rightArray[j]
            j = j + 1
            k = k + 1
        elif leftArray[i] == rightArray[j]:
            a[k] = leftArray[i]
            i = i + 1
            k = k + 1
            a[k] = rightArray[j]
            j = j + 1
            k = k + 1
    while i < len(leftArray):
        a[k] = leftArray[i]
        i = i + 1
        k = k + 1
        
    while j < len(rightArray):
        a[k] = rightArray[j]
        j = j + 1
        k = k + 1
#     print(a)
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
MergeSort(a)
print(a)