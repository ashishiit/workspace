'''
Created on Jan 22, 2017

@author: S528358
'''
a = 'test'
count = [0]*26
for i in a:
#     print(ord(i)-'a')
    count[ord(i)-ord('a')] = count[ord(i)-ord('a')]+1
max_count = -1
for i in a:
    if count[ord(i)-ord('a')] > max_count:
        temp = i
print('max occouring character = %s'%i)