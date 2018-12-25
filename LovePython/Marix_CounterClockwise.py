'''
Created on Jan 22, 2017

@author: S528358
'''
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
top = 0
bottom = len(a)
left = 0
right = len(a)
while top<bottom and left<right:
    previous = a[top+1][right-1]
    print('previous = %d'%previous)
    for i in range(right-1, top-1, -1):
        current = a[top][i]
        a[top][i] = previous
        previous = current
    top = top + 1
    print('previous = %d'%previous)
    for i in range(top, bottom):
        current = a[i][left]
        a[i][left] = previous
        previous = current
    left = left + 1
    print('previous = %d'%previous)
    for i in range(left, right-1):
        current = a[bottom-1][i]
        a[bottom-1][i] = previous
        previous = current
    bottom = bottom - 1
    print('previous = %d'%previous)
    for i in range(bottom, top-1, -1):
        current = a[i][right-1]
        a[i][right-1] = previous
        previous = current
    right = right - 1
#     break
print(a)