'''
Created on Jul 2, 2017

@author: S528358
'''
def InsertionSort(alist):
    count = 0
    for i in range(1,len(alist)):
        temp = alist[i]
        while i>0 and alist[i-1]>temp:
            count = count + 1
            alist[i]=alist[i-1]
            i = i - 1
        alist[i] = temp
    print(alist)
    print(count)
    
alist = [1, 3, 9, 8, 2, 7, 5]
InsertionSort(alist)