'''
Created on Jan 21, 2017

@author: S528358
'''
a = [42, 89, 63, 12, 94, 27, 78, 3, 50, 36]
pivot = a[len(a)-1]
def Swap(left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
left = 0
right = len(a)-2

while True:
    while a[left] < pivot:
        left = left + 1
    while a[right] > pivot:
        right = right - 1
    if left < right:
        Swap(left, right)
    else:
        break
Swap(left, len(a)-1)
print(a)
