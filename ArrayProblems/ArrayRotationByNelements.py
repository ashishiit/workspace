'''
Created on Sep 15, 2018

@author: S528358
'''
def Solution(a,low,high):
    while low < high:
        temp = a[high]
        a[high] = a[low]
        a[low] = temp
        low = low + 1
        high = high - 1
a = [1, 2, 3, 4, 5, 6, 7]
Solution(a,0,len(a)-1)
d = 2
Solution(a,0,len(a)-1-d)
Solution(a,len(a)-d,len(a)-1)
print(a)
