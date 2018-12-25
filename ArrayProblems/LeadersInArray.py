'''
Created on Jun 10, 2018

@author: S528358
'''
def Leaders(a):
    temp = a[len(a)-1]
    print(temp)
    for i in range(len(a)-2, -1, -1):
        if a[i] > temp:
            print(a[i])
            temp = a[i]
    

a = [16, 17, 4, 3, 5, 2]
Leaders(a)