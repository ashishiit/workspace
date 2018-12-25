'''
Created on Nov 11, 2018

@author: S528358
'''
fact = []
fact.append(1)
for i in range(1,6):
    fact.append(i*fact[i-1])
print('factorial of 5 is',fact[5])