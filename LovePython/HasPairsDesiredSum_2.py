'''
Created on Jan 18, 2017

@author: S528358
'''
total = 16
a = [1, 4, 45, 6, -8, 10]
temp = []
for i in a:
    if total-i in temp:
        print('%d and %d'%(total-i,i))
    else:
        temp.append(i)