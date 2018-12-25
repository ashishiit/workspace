'''
Created on Jul 4, 2017

@author: S528358
'''
a = [3, 1, 5, 2]
c=[None]*len(a)
# k = 0
def Sort(a, left, right):
#     c = []
    k = 0
    mid = (left+right)//2
    if left<right:
        print(left, right)        
        Sort(a, left, mid)
        Sort(a, mid+1, right)
        
    i = left
    j = mid+1
    
    
    while i<=mid and j<=right:
        
        if a[i] < a[j]:                
            c[k] = a[i]
            
            i = i + 1
        else:
            c[k] = a[j]
            j = j + 1
        k = k + 1
            
    while i <= mid:
        c[k] = a[i]
        i = i + 1
        k = k + 1
    while j <= right:
        c[k] = a[j]
        j = j + 1
        k = k + 1
    k=0
    print(c)
    while left <= right:
        a[left] = c[k]
        left = left + 1
        k = k + 1
            
    return a

print(Sort(a, 0, len(a)-1))