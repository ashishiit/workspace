'''
Created on Jan 21, 2017

@author: S528358
'''
a = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
'''row'''
k = 0
m = len(a)
'''column'''
l = 0
n = len(a[0])
while k < m and l < n:
    for i in range(l,n):
        print(a[k][i],end = ' ')
    k = k + 1
    for i in range(k,m):
        print(a[i][n-1],end = ' ')
    n = n - 1
    if k < m:
        for i in range(n-1, l, -1):
            print(a[m-1][i],end = ' ')
    m = m - 1
    if l < n:
        for i in range(m, k-1, -1):
            print(a[i][l],end = ' ')
    l = l + 1
