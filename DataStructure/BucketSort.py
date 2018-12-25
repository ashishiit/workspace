'''
Created on Jul 1, 2017

@author: S528358
'''
a = [31415926535897932384626433832795, 1, 3, 10, 3, 5]
d = {}
for i in a:
    length = len(str(i))
    if length not in d:
        d[length] = []
    d[length].append(i)
for i in sorted(d):
    for j in sorted(d[i]):
        print(j)