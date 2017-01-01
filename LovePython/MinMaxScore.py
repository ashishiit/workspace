'''
Created on Oct 29, 2016

@author: s528358
'''
a = int(input())
b = int(input())
min_count = 0
max_count = 0
count_loop = 0
while a <= b:
#     print(count_loop)
#     print('a = %d'%a)
    str_a = str(a)
    str_b = str(b)
    if len(str_a)>=3 or len(str_b)>=3:
        left = 1
        right = len(str_a)-2
        while left <= right:
            if int(str_a[left])<int(str_a[left-1]) and int(str_a[left])<int(str_a[left+1]):
#                 print('first else')
#                 print ('%d   %d   %d'%(int(str_a[left-1]), int(str_a[left]), int(str_a[left+1])))
                min_count = min_count + 1
            elif int(str_a[left])>int(str_a[left-1]) and int(str_a[left])>int(str_a[left+1]):
#                 print('second else')
#                 print ('%d   %d   %d'%(int(str_a[left-1]), int(str_a[left]), int(str_a[left+1])))
                max_count = max_count + 1
            left = left + 1
    count_loop = count_loop + 1
    a = a + 1
    
total = min_count + max_count
# print('count loop = %d'%count_loop)
print(total)
