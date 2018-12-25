'''
Created on Jan 2, 2017

@author: S528358
'''
a = [10, 22, 9, 33, 21, 50, 41, 60, 83]
s = [1]*len(a)
# print('original subsequence = %d',s)
for i in range(1, len(a)):
    test = []
    for j in range(0, i):
        if a[i] > a[j]:
            s[i] = max(s[i], s[j]+1)
# print(s)
print('maximum subsequence length = %d'%max(s))