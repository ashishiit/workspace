'''
Created on Oct 7, 2018

@author: S528358
'''
a = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
temp = 0
result = {}
for i in range(len(a)):
    if a[i] not in result:
        result[a[i]] = i
    else:
        if i-result[a[i]] > temp:
            temp = i - result[a[i]]
print(temp)