'''
Created on May 23, 2018

@author: s528358

1. assumption: assumed numbers from 0 to 999
2. initialize total = 0
3. loop for numbers from 0 to 999
4. for each number, increment total by 1 if number divisible by 3.
5. for each number, increment total by 1 if number divisible by 5.
6. total gives the sum of all multiples of 3 or 5 less than 1000, that is 0 to 999.
'''
total = 0
for i in range(1000):
    if i%3==0:
        total = total + 1
    if i%5==0:
        total = total + 1
print('sum of multiples of 3 or 5 =',total)