'''
Created on Jun 3, 2018

@author: S528358
'''
a = [3, 4, -1, 0, 6, 2, 3]
temp = [1]*len(a)
for i in range(1, len(a)):
    j = 0
    while j < i:
        if a[j] < a[i]:
            temp[i] = max(temp[j]+1, temp[i])
        j = j + 1
print('length of longest increasing subsequence =', max(temp))