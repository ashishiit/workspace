'''
Created on Dec 18, 2016

@author: S528358
'''
a = [1, 2, 3, 4, 22]
b = [-20, 30]
c = []
i = 0
j = 0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    elif b[j]<a[i]:
        c.append(b[j])
        j=j+1
    else:
        i = i + 1
        j = j + 1
print(c)