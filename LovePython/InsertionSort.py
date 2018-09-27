'''
Created on Dec 21, 2016

@author: S528358
'''
# count = 0

    
    
a = [1, 10, -67, -2, 2]
def Solution(L, temp):
    count = 0
    for i in range(1, len(a)):
        j = i
        temp = a[i]
    
        while j>0 and a[j-1]>temp:
#             count = count + 1
            a[j] = a[j-1]
            j = j - 1
            a[j] = temp
# print('number of shifts = %d'%count)
#     print('insertion sorted')
    return a
from time import perf_counter
import random
a = [1, 10, -67, -2, 2]
N = 100
ITERS = 1000
elapsed = 0
for i in range(ITERS):
    L = random.sample(range(1,N),99)
    start = perf_counter()
    Solution(a,L,N//2)
    end = perf_counter()
    elapsed += (end - start)
print('sorting algorithm',elapsed/N,'s')
    
    
print(Solution(a, L, N//2))    
    

