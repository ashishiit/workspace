'''
Created on Dec 22, 2016

@author: S528358
'''
T = int(input())
for k in range(T):
    count = 0
    a = []
#     print(a)
    N = int(input())
    #a = [int(y) for y in input().split(' ')]
    a = [x for x in input().split(" ")]
    print(a)
    #print(a)
    for i in range(1, N):
        temp = a[i]
        j = i
        while j>0 and a[j-1]>temp:
            count = count + 1
            a[j] = a[j-1]
            j = j - 1
        a[j] = temp
    print(count)