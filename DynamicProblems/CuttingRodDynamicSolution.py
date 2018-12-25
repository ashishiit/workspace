'''
Created on Jun 2, 2018

@author: S528358
'''
W = 5
w = [1, 2, 3, 4]
v = [2, 5, 7, 8]

weight = [i for i in range(W+1)]
# print(weight)
# temp = [[0]*(W+1)]*len(w)
temp = [[0 for i in range(W+1)] for j in range(len(w))]

for i in range(W+1):
    temp[0][i] = weight[i]*v[0]
   
# print(temp) 
for i in range(1, len(w)):
    for j in range(1, W+1):
        if w[i] > weight[j]:
            temp[i][j] = temp[i-1][j]
        else:
            temp[i][j] = max(v[i]+temp[i][weight[j]-w[i]], temp[i-1][j])
print('maximum value = ',temp[len(w)-1][W])

