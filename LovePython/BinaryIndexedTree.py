'''
Created on Dec 23, 2016

@author: S528358
'''
# a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
a = []
for i in range(10000001):
    a.append(i)
BIT = [0]*(len(a)+1)
def Traditional(a):
    total = 0
    for i in a:
        total = total + i
    return total
def getSum(index):
    index = index + 1
    total = 0
    while index > 0:
        total = total + BIT[index]
        index = index - (index & (-index))
    return total
def UpdateBIT(BIT, n, i, value):
    i = i + 1
    while i <= n:
        BIT[i] = BIT[i] + value
        i = i + (i & (-i))
#     print(BIT)
for i in range(len(a)):
    UpdateBIT(BIT, len(a), i, a[i])
# print('sum = %d'%getSum(len(a)-1))
print('traditional sum double check = %d'%Traditional(a))