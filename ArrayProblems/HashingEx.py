'''
Created on Oct 7, 2018

@author: S528358
'''
a = [1, 4, 45, 6, 10, 8]
result = []
target = 16
for i in a:
    if target-i in result:
        print([i, target-i])
    else:
        result.append(i)