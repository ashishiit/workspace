'''
Created on Oct 28, 2016

@author: s528358
'''
def Factorial(num):
    if num == 0:
        return 1
    else:
        result = num * Factorial(num-1)
    return result
print('result = %d'%Factorial(4))