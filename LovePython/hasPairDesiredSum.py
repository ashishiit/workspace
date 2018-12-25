'''
Created on Jan 4, 2017

@author: S528358
'''
a = [1, 4, 45, 6, 10, 8]
b = sorted(a)
sum = 1
def Solution_2(a):
    hash_table = [0]*(max(a)+1)
    for i in a:
        temp = sum - i
        if hash_table[temp] == 1:
            return True
        else:
            hash_table[i] = 1
    return False
def Solution_1(b):
    left = 0 
    right = len(b)-1
    while left < right:
        if b[left]+b[right] < sum:
            left = left + 1
        elif b[left]+b[right] > sum:
            right = right - 1
        elif b[left]+b[right] == sum:
            return True
    return False
# print(Solution_1(b))
print(Solution_2(a))
    
    
    