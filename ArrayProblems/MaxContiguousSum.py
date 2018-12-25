'''
Created on Jun 10, 2018

@author: S528358
'''
def MaxContiguousSum(a):
    s = []
    s.append(a[0])
    for i in range(1, len(a)):
        s.append( max(s[i-1]+a[i], a[i]))
    
    return max(s)
    
a = [2, 3, 4, 1, 2, 1, 5, 3]
print('max contiguous sum = ',MaxContiguousSum(a))