'''
Created on Sep 21, 2018

@author: S528358
'''
def Solution(a):
    result = {}
    for i in a:
        if i not in result:
            result[i] = 1
        else:
            result[i] = result[i] + 1
    for i in result:
        if result[i] == 1:
            print (i)
a = [7, 7, 8, 8, 9, 1,1, 4, 2,2]
Solution(a)