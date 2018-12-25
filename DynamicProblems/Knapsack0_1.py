'''
Created on Dec 28, 2017

@author: S528358
'''
W = 7
w = [1, 3, 4, 5]
v = [1, 4, 5, 7]

temp = [[0 for i in range(W+1)] for j in range(len(w))]

weight = [i for i in range(W+1)]

for i in range(1, W+1):
    temp[0][i] = v[0]
    
for i in range(1, len(w)):
    for j in range(1, W+1):
        if w[i] > weight[j]:
            temp[i][j] = temp[i-1][j]
        else:
            temp[i][j] = max(v[i]+temp[i][weight[j]-w[i]], temp[i-1][j])
print('maximum value = ', temp[len(w)-1][W])