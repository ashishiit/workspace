'''
Created on Oct 28, 2016

@author: s528358
'''
def BinarySearch(item):
    a = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    left = 0
    right = len(a) - 1
    while left < right:
        mid = (left+right)//2
        if a[mid] == item:
            return mid
        elif item > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
result = BinarySearch(260)
if result == -1:
    print('item not found')
else:
    print('FOUND')