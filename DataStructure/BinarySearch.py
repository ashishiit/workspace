'''
Created on Jun 24, 2017

@author: S528358
'''
def BinarySearch(testlist, item):
    left = 0
    right = len(testlist)-1
    while left < right:
        mid = (left+right)//2
        if testlist[mid] == item:
            return True
        elif item > testlist[mid]:
            left = mid + 1
        elif item < testlist[mid]:
            right = mid - 1
    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BinarySearch(testlist, 32))