'''
Created on Jan 5, 2017

@author: S528358
'''
a = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
left = 0
right = len(a) - 1
def Swap(a, left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
while True:
    while a[left] == 0:
        left = left + 1
    while a[right] == 1:
        right = right - 1
    if left < right:
        Swap(a, left, right)
    else:
        break
print(a)
