'''
Created on Dec 21, 2016

@author: S528358
'''
count = 0

a = [1, 1, 1, 2, 2]
for i in range(1, len(a)):
    j = i
    temp = a[i]
    
    while j>0 and a[j-1]>temp:
        count = count + 1
        a[j] = a[j-1]
        j = j - 1
    a[j] = temp
print('number of shifts = %d'%count)
print('insertion sorted')
print(a)
