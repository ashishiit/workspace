'''
Created on Jan 21, 2017

@author: S528358
'''
a = [[10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
target = 29
row = 0
column = len(a)-1
def Solution(a, row, column):
    while row<len(a) and column>=0:
        if a[row][column] == target:
            return 'Found'
        elif a[row][column] > target:
            column = column - 1
        else:
            row = row + 1
    return 'Not Found'
    
    
    
result = Solution(a, row, column)
print(result)
    