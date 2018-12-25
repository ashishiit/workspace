'''
Created on Aug 3, 2018

@author: s528358
'''
a = [5, 10, 15]
b = [2, 3, 20, 40, 50]
c = []
i = 0
j = 0
while i<len(a) and j<len(b):
    if a[i] == b[j]:
        c.append(a[i])
        i = i + 1
        j = j + 1
    elif a[i] < b[j]:
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
print(c)