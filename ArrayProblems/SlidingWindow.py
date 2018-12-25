'''
Created on May 21, 2018

@author: S528358
'''
a = [1, 4, 2, 10, 23, 3, 1,0, 20]
k = 4
max_sum = 0
for i in range(k):
    max_sum = max_sum + a[i]
# print(max_sum)
for i in range(1, len(a)):
    if i+k-1 <= len(a)-1:
        win_sum = max_sum - a[i-1] + a[i+k-1]        
        max_sum = max(max_sum, win_sum)
    else:
        break
print(max_sum)