'''
Created on Jun 24, 2017

@author: S528358
'''
def BubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    print(alist)
alist = [54,26,93,17,77,31,44,55,20]
BubbleSort(alist)