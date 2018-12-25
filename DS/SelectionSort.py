'''
Created on Jun 25, 2017

@author: S528358
'''
'''1. find position of the maximum element
   2. swap this position with the position of the last element
   '''
def SelectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        position = 0
        for j in range(1, i+1):
            if alist[j] > alist[position]:
                position = j 
        temp = alist[i]
        alist[i] = alist[position]
        alist[position] =  temp
    print(alist)          
alist = [54,26,93,17,77,31,44,55,20]
SelectionSort(alist)