'''
Created on Jun 9, 2018

@author: S528358
'''
def MaxEquilibrium(a):
    left = 0
    right = sum(a)
    for i in range(len(a)):
        if left>=right :
            return left
        left = left + a[i]
        right = right - a[i]
a = [-2, 5, 3, 1, 2, 6, -4, 2]
print('equilibrium sum = ', MaxEquilibrium(a))