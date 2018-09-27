'''
Created on Oct 29, 2016

@author: s528358
'''
def Fact(n):
    if n == 0:
        return 1
    else:
        result = n * Fact(n-1)   

print(Fact(4))