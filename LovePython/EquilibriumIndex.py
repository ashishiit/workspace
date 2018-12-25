'''
Created on Jan 5, 2017

@author: S528358
'''


def Equilibrium():
    a = [-7, 1, 5, 2, -4, 3, 0]
    leftsum = 0
    rightsum = 0
    for i in a:
        rightsum = rightsum + i
    for i in range(len(a)):
        rightsum = rightsum - a[i]
        if leftsum == rightsum:
           return i
        else:
           leftsum = leftsum + a[i]
    return -1
print(Equilibrium())