'''
Created on May 26, 2017

@author: S528358
'''
MOD = 1000000007
import math
def power_new(a,b):
    print ('this function is called')
    result = 1
    while b > 0:
        if b%2 == 1:
            result = (result * a) % MOD
        b = b / 2
        a = (a*a)%MOD
    return result
def power_function(base, num):
    temp = 0
    if num == 0:
        return 1
    temp = power_function(base, num//2)
    if num%2 == 0:
        return temp*temp
    else:
        return base*temp*temp
def Solution(inp, base):
    num = len(inp)
    i = 0
    num = num - 1
    count = 0
    while i<len(inp) and num>=0:
        count = count + int(inp[i])*power_new(base,num)
        i = i + 1
        num = num - 1
    return int(count)

s = '1'*300000
i = 0
j = 30000
count = 0
while j <= len(s):
    temp = s[i:j]
    print (temp)
#     count = count + Solution(temp, k , b, m)
    #print (count)
    i = i + 1
    j = j + 1
    
    
# test = '0'*300000
# print(test)
# print(Solution(test, 2))
# print(power_new(2,2))
# a = {}
# i = 0
# j = 5000
# k = 5001
# l = 10000
# 
# while i <= j and k <= l:
#     a[i] = k
#     i = i + 1
#     k = k + 1
# print(a)
# print(a[len(a)-1])
