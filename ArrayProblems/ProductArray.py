'''
Created on May 20, 2018

@author: S528358
'''
a = [10, 3, 5, 6, 2]
temp = 1
left = []
right = []
for i in range(len(a)):
    left.append( temp)
    temp = temp * a[i]

temp = 1
right = [1]*len(a)
for i in range(len(a)-1, -1, -1):
    right[i] =  temp
    temp = temp * a[i]
    
for i in range(len(a)):
    print(left[i]*right[i])