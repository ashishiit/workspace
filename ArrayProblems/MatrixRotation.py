'''
Created on Oct 8, 2018

@author: S528358
'''
s = [[1,2], [3,4], [5,6]]
s_row = len(s)
s_column = len(s[0])

d = []


for i in range(s_column):
    temp = []
    for j in range(s_row):
        temp.append(s[j][i])
    d.append(temp)
print(s)
print(d)