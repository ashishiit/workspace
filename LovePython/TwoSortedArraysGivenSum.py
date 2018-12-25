'''
Created on Jan 15, 2017

@author: S528358
'''
a = [1, 3, 5, 6, 7, 8, 10, 13, 14]
b = [1, 2, 3, 4, 5, 18]
total = 10
i = 0
j = len(b)-1
while i < len(a) and j >= 0:
    if a[i]+b[j] == total:
        print('%d and %d'%(a[i],b[j]))
        i = i + 1
        j = j - 1
    elif a[i]+b[j] < total:
        i = i + 1
    elif a[i]+b[j] > total:
        j = j - 1
