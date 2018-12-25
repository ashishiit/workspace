'''
Created on Aug 10, 2017

@author: S528358
'''
print('Hello Python')
temp = []
temp.append(0)
temp.append(1)
for i in range(2,13):
    temp.append(temp[i-1]+temp[i-2])
print(temp)