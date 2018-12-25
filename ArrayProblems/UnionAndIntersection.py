'''
Created on Dec 28, 2017

@author: S528358
'''
def Union(a, b):
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
    while i < len(a):
        c.append(a[i])
        i = i + 1
    while j < len(b):
        c.append(b[j])
        j = j + 1
    return c
def Intersection(a, b):
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            i = i + 1
        elif b[j] < a[i]:
            j = j + 1
        else:
            c.append(a[i])
            i = i + 1
            j = j + 1
    return c
a = [1, 3, 4, 5, 7]
b = [2, 3, 5, 6]
print('union = ',Union(a, b))
print('intersection = ', Intersection(a, b))
