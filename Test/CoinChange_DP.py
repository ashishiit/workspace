'''
Created on Dec 15, 2017

@author: s528358
'''
a = []
for i in range(3):
    temp = []
    for j in range(12):
        temp.append(0)
    a.append(temp)
for i in range(1, 12):
    a[0][i] = i
# print(a)
coins = [1, 3, 5]
for i in range(1, 3):
    for j in range(1, 12):
        if coins[i] > j:
            a[i][j] = a[i-1][j]
        else:
            a[i][j] = min(a[i-1][j], a[i][j-coins[i]]+1)

for i in range(12):
    print('min number of coins for %d is %d'%(i,a[2][i]))