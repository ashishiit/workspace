'''
Created on Dec 15, 2017

@author: S528358
'''
coins = [8, 3, 1, 2]
a = []
for i in range(4):
    temp = []
    for j in range(4):
        temp.append(0)
    a.append(temp)
# print(a)
for i in range(4):
    a[i][0] = 1
# print(a)
for i in range(4):
    for j in range(1, 4):
        if coins[i] > j and i==0:
            a[i][j] = 0
        else:
            a[i][j] = a[i-1][j] + a[i][j-coins[i]]
# print(a)
print('# of coins to get sum of 3 is = ',a[3][3])