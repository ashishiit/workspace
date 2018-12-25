'''
Created on Jun 10, 2017

@author: S528358
'''
a = [1, 2, 3]
k = 2
for i in range(k):
    temp = a.pop()
    a.insert(0,temp)
print(a)