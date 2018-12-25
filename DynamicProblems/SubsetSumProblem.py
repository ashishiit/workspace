'''
Created on Jun 4, 2018

@author: S528358
'''
S = 11
v = [2, 3, 7, 8, 10]
sums = [i for i in range(S+1)]
print(sums)
temp = [[0 for i in range(S+1)] for j in range(len(v))]
# print(temp)
for i in range(len(v)):
    temp[i][0] = 1
# print(temp)
for i in range(1,S+1):
    if v[0] == sums[i]:
        temp[0][i] = 1
    else:
        temp[0][i] = 0
# print(temp) 
for i in range(1,len(v)):
    for j in range(S+1):
        if v[i] > sums[j]:
#             print(v[i], sums[j])
            temp[i][j] = temp[i-1][j]
        else:
            temp[i][j] = temp[i-1][j] + temp[i-1][sums[j]-v[i]]
# print(temp)   
if temp[len(v)-1][S] != 0:
    print('subset NOT present')
else:
    print('subset sum is there')                      