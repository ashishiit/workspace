'''
Created on Oct 29, 2017

@author: S528358
'''
sum_var = 0
count = 0
def Solution(X,num):
    if X == 0:
        return
    temp = pow(X,num)
    if temp > X_inp:
        temp = 0
    sum_var = sum_var + temp
    if sum > X_inp:
        sum_var = sum_var - temp
    if sum == X_inp:
        count = count + 1
    Solution(X-1, num)
X_inp = int(input())
num = int(input())
Solution(X_inp, num)
print(count)