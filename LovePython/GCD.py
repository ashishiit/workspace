'''
Created on Jul 19, 2017

@author: S528358
'''
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)
a = int(input())
b = int(input())
result = gcd(a, b)
print(result)

