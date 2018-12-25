'''
Created on Jan 18, 2017

@author: S528358
'''
a = [7, 9, 5, 6, 3, 2]
minimum = a[0]
max_diff = a[1] - a[0]
for i in range(2, len(a)):
    if a[i]-minimum > max_diff:
        max_diff = a[i]-minimum
    if a[i] < minimum:
        minimum = a[i]
print('max diff = %d'%max_diff)