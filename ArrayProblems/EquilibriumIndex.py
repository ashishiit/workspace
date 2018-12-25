'''
Created on Jun 9, 2018

@author: S528358
'''
def EquilibriumIndex(a):
    left = 0
    right = sum(a)
    for i in range(len(a)):
        right = right - a[i]
        if left == right:
            return i
        left = left + a[i]
    return -1
a = [-7, 1, 5, 2, -4, 3, 0]
print('equilibrium index = ', EquilibriumIndex(a))