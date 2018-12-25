'''
Created on Jun 9, 2018

@author: S528358
'''
def Search(a,num):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = (left+right)//2
        if a[mid] == num:
            return 'Found'
        elif num > a[mid]:
            left = mid + 1
        elif num < a[mid]:
            right = mid - 1
    return 'Not Found'

def Insert(a, num):
    i = 0
    while i < len(a):
        if num < a[i]:
            break
        else:
            i = i + 1
    a.insert(i,num)
    return a
arr = [5,6,7,8,9,10]
print(Search(arr, 1))
print(Insert(arr,50))