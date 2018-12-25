'''
Created on Jun 10, 2017

@author: S528358
'''
a = [100, 50, 40, 20, 10]
num = 50
start = 0
end = len(a)
if num < a[len(a)-1]:
    print( len(a)+1)
elif num > a[0]:
    print(1)
else:
    start = 0
    end = len(a)-1
    
    while start <= end:
        mid = (start+end)//2
        if (num>a[mid] and num<a[mid-1]) or num==a[mid]:
            print(mid+1)
            break
        elif num>a[mid]:
            end = mid-1
        elif num<a[mid]:
            start = mid+1
        