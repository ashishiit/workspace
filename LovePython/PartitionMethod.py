'''
Created on Jan 21, 2017

@author: S528358
'''
a = [149, 192, 47, 152, 159, 195, 61, 66, 17, 167, 118, 64, 27, 80, 30, 105]
pivot = 99
left = 0
right = len(a)-1
def Swap(left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
while True:
    while a[left]<pivot:
        left = left + 1
    while a[right] > pivot:
        right = right - 1
    if left < right:
        Swap(left,right)
    else:
        break
print(a)
    