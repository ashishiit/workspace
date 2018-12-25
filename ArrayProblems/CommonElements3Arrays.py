'''
Created on Jun 9, 2018

@author: S528358
'''

def CommonElements(a, b, c):
    i = 0
    j = 0
    k = 0
    while i<len(a) and j<len(b) and k<len(c):
        if a[i]==b[j] and b[j]==c[k]:
            print(a[i])
            i = i + 1
            j = j + 1
            k = k + 1
        elif a[i] < b[j]:
            i = i + 1
        elif b[j] < c[k]:
            j = j + 1
        else:
            k = k + 1
    if i==len(a) and j==len(b) and k==len(c):
        print('no common elements')
a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]
CommonElements(a, b, c)
