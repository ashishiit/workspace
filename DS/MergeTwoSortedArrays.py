'''
Created on Jun 25, 2017

@author: S528358
'''
'''merge two sorted arrays'''

def Merge(a, b):
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
        
    while i<len(a):
        c.append(a[i])
        i = i + 1
    while j<len(b):
        c.append(b[j])
        j = j + 1
    print(c)
    
a = [23, 47, 81, 95]
b = [7, 14, 39, 55, 62, 74]
Merge(a, b)