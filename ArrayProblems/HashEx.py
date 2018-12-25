'''
Created on Oct 7, 2018

@author: S528358
'''
a = [4, 3, 4, 4, 2, 4]
result = {}
for i in a:
    if i not in result:
        result[i] = 1
    else:
        result[i] = result[i] + 1

count = 0
for i in result:
    if result[i] == 1:
        count = count + 1
print(count)