'''
Created on Jul 8, 2017

@author: S528358
'''
# count = 0
def Swap(ar, leftPtr, rightPtr):
    temp = ar[leftPtr]
    ar[leftPtr] = ar[rightPtr]
    ar[rightPtr] = temp
def Partition(ar, left, right):
#     count = 0
    leftPtr = left
    rightPtr = right - 1
    pivot = ar[right]
    for j in range(left, right):
        if ar[j] <= pivot:
#             count = count + 1
            
            Swap(ar, leftPtr, j)
            leftPtr = leftPtr + 1
            
            
    Swap(ar, leftPtr, right)
#     count = count + 1
#     print(count)
#     count = count + leftPtr
#     print(count)
    return leftPtr
        
#     count = 0
#     pivot = ar[right]
#     leftPtr = left
#     rightPtr = right - 1
#     while True:
#         while ar[leftPtr] < pivot:
#             leftPtr = leftPtr + 1
#         while ar[rightPtr] > pivot:
#             rightPtr = rightPtr - 1
#         if leftPtr > rightPtr:
#             break
#         else:
#             count = count + 1
#             print(ar)
#             Swap(ar, leftPtr, rightPtr)
#             print(ar)            
#     Swap(ar, leftPtr, right)
#     print(count)
# ar = [1, 3, 9, 8, 2, 7, 5]
count = 0
def Sort(a, leftPtr, rightPtr,count):
#     print(count)
    if leftPtr < rightPtr:
#         count = count + 1
        part = Partition(a, leftPtr, rightPtr)
        count = count + part
        Sort(a, leftPtr, part-1,count)
        Sort(a, part+1, rightPtr,count)
        print(a)
#     print(count)
a = [1, 3, 9, 8, 2, 7, 5]
Sort(a, 0, len(a)-1,0)
# print(a)
# print(count)