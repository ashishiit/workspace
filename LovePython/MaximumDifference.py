'''
Created on Jan 4, 2017

@author: S528358
'''
a = [7, 6, 4, 3, 1]
max_number = a[1] - a[0]
'''brute force approach'''
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i] > max_number:
            max_number = a[j] - a[i]
print('first method = %d'%max_number)

'''efficient method'''
min_number = a[0]
max_diff = a[1]-a[0]
for i in range(1, len(a)):
    if a[i]-min_number > max_diff:
        max_diff = a[i]-min_number
    if a[i]<min_number:
        min_number = a[i]
print('second method = %d'%max_diff)