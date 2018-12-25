'''
Created on Jun 9, 2018

@author: S528358
'''
def PairSum(a,target):
    temp = []
#     result = []
    for i in a:
        if target-i in temp:
            print(i,'and',target-i)
        else:
            temp.append(i)
    
a = [1,-4, -45, 6, 10, 8]
target = 16
PairSum(a,target)