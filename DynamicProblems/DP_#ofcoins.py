'''
Created on Dec 29, 2017

@author: S528358
'''
val = [1, 2, 5]
W = 11

result = [[0]*(W+1) for i in range(len(val))]
for i in range(1, W+1):
    result[0][i] = i
    
for i in range(1, len(val)):
    for j in range(1, W+1):
#         print('val, W',val[i],W)
        if val[i] > j:
            
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = min(1+result[i][j-val[i]], result[i-1][j])
print(result)
print('minimum coins for sum 11 = ',result[len(val)-1][W])