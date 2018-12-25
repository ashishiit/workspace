'''
Created on Aug 19, 2017

@author: S528358
'''
a = [20, 580, 420, 900]
k = 3
i = 0
temp = []
n = len(a)
count = 0

while count < k and i < n:
    total = 0        
    while i<n-1 and a[i+1] <= a[i]:
        i = i + 1
    buy = i
    print('buy= ',a[buy])
    i = i + 1
    while i<n and a[i] >= a[buy]:
#         total = a[i]-a[buy]
        i = i + 1
    sell = i - 1
    print('sell= ',a[sell])
#     print(a[sell]-a[buy])
    print('------')
    temp.append(a[sell]-a[buy])
    count = count + 1
print(sum(temp))
