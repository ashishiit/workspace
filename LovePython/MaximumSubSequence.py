'''
Created on Jan 1, 2017

@author: S528358
'''
a = [-2, -3, 4, -1, -2, 1, 5, -3]
s = [None]*len(a)
s[0] = a[0]
for i in range(1, len(a)):
    s[i] = max(s[i-1]+a[i], a[i])
print('maximum contiguous subsequence =%d'%max(s))