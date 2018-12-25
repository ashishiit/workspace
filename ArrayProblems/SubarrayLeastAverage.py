'''
Created on Jun 11, 2018

@author: S528358
'''
def SubArrayLeastAverage(a):
    min_sum = a[0]+a[1]
    min_avg = min_sum//2
    for i in range(1, len(a)-1):
        if min_sum-a[i-1]+a[i+1] < min_sum:
            min_sum = min_sum-a[i]+a[i+1]
            min_avg = min_sum//2
    print('least average = ', min_avg)
a = [3, 7, 5, 20, -10, 0, 12]
SubArrayLeastAverage(a)