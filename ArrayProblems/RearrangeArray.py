'''
Created on Oct 9, 2018

@author: S528358
'''
a = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
temp = []
for i in a:
    temp.append(i)
for i in range(len(a)):
    if i in temp:
        a[i] = i
    else:
        a[i] = -1
print(a)