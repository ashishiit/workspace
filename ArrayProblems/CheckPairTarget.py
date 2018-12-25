'''
Created on Oct 9, 2018

@author: S528358
'''
def CheckPair(a):
    result = []
    target = 16
    for i in a:
        if target-i in result:
            return True
        else:
            result.append(i)
    return False

a = [1, 4, 45, 6, 10, -8]

print(CheckPair(a))
