'''
Created on Dec 20, 2016

@author: S528358
'''
# a = []
def Sort(a):
    if len(a)>1:
        mid = len(a) //2
        left = Sort(a[:mid])
        right = Sort(a[mid:])
        return Merge(a,left,right)
    else:
        return a
def Merge(a,left,right):
#     c = []
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
#             k = k + 1
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
#             k = k + 1
        k = k + 1
    print(a)
    while i < len(left):
        a[k] = left[i]
        k = k + 1
        i = i + 1
    while j < len(right):
        a[k] = right[j]
        k = k + 1
        j = j + 1
    return a
print(Sort([3, 1, 5, 2]))