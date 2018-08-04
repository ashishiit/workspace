'''
Created on Aug 3, 2018

@author: s528358
'''
def MergeSort(a):
    print('control flow =',a)
    if len(a)==1:
        return
    else:
        mid = len(a)//2
        print('mid = ',mid)
        left = a[:mid]
        right = a[mid:]
        print('left = ',left)
        print('right = ',right)
        MergeSort(left)
        MergeSort(right)
        
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i = i + 1
            else:
                a[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            a[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            a[k] = right[j]
            j = j + 1
            k = k + 1
        print('a = ',a)
a = [64, 21, 33, 70]
MergeSort(a)
print('sorted elements = ',a)
