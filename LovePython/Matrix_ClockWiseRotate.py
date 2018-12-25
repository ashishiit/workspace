'''
Created on Jan 21, 2017

@author: S528358
'''
# from tkinter.constants import CURRENT
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
left = 0
right = len(a)
top = 0
bottom = len(a)
# previous = a[top+1][left]
# print('previous = %d'%previous)
while top < bottom and left < right:
#     print('previous = %d'%previous)
    previous = a[top+1][left]
    print('previous = %d'%previous)
    for i in range(left,right):
        current = a[top][i]
        a[top][i] = previous
        previous = current
    top = top + 1
    print('previous = %d'%previous)
    for i in range(top, bottom):
        current = a[i][right-1]
        a[i][right-1] = previous
        previous = current
    right = right - 1
    print('previous = %d'%previous)
    for i in range(right-1, left, -1):
        current = a[bottom-1][i]
        a[bottom-1][i] = previous
        previous = current
    bottom = bottom - 1
    print('previous = %d'%previous)
    for i in range(bottom, top-1, -1):
        current = a[i][left]
        a[i][left] = previous
        previous = current
    left = left + 1
print(a)