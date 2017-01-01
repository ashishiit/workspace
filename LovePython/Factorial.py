'''
Created on Oct 29, 2016

@author: s528358
'''
def Fact(n):
    if n == 1:
        return 1
    else:
        result = 2*Fact(n-1)+1
    return result
print(Fact(4))