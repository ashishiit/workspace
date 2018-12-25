'''
Created on Jan 21, 2017

@author: S528358
'''
a = [7, 10, 4, 3, 20, 15]
target = 3

def Swap(a, left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
# def Partition(a, left, right):
#     leftPtr = left
#     rightPtr = right - 1
#     pivot = a[right]
#     while True:
#         while a[leftPtr] < pivot:
#             leftPtr = leftPtr + 1
#         while a[rightPtr] > pivot:
#             rightPtr = rightPtr - 1
#         if leftPtr < rightPtr:
#             Swap(a, leftPtr, rightPtr)
#         else:
#             break
#     Swap(a, leftPtr, right)
#     return leftPtr
def Solution(a, left, right, k):
#     parition = Partition(a, left, len(a))
#     print('test')
    print(k)
    pivot = a[right]
    leftPtr = left
    rightPtr = right - 1
    while True:
        while a[leftPtr] < pivot:
            leftPtr = leftPtr + 1
        while a[rightPtr] > pivot:
            rightPtr = rightPtr - 1
        if leftPtr < rightPtr:
            Swap(a, leftPtr, rightPtr)
        else:
            break
        
    Swap(a, leftPtr, right)
    if leftPtr == k - 1:
        return a[leftPtr]
    elif leftPtr > k-1:
        return Solution(a, left, leftPtr-1, k)
    else:
        return Solution(a, leftPtr+1, right, k)
# partition = Partition(a, 0, len(a)-1)
# print('partition = %d'%partition)
s = Solution(a, 0, len(a)-1, 5)
print('%d th smallest/largest is = %d'%(target,s))