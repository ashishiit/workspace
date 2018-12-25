'''
Created on Jun 4, 2018

@author: S528358
'''
a = [2, -1, 4, 3, 5, -1, 3, 2]
left = [1]*len(a)
right = [1]*len(a)
temp = []
for i in range(1, len(a)):
    j = 0
    while j < i:
        if a[j] < a[i]:
            left[i] = max(left[i], left[j]+1)
        j = j + 1

for i in range(len(a)-2, -1, -1):
    j = len(a)-1
    while j > i:
        if a[j] < a[i]:
            right[i] = max(right[i], right[j]+1)
        j = j - 1


for i in range(len(a)):
    temp.append(left[i]+right[i]-1)
print('length of longest bitonic sequence = ',max(temp))