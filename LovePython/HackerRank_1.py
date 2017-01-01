'''
Created on Nov 4, 2016

@author: s528358
'''
import math
# from _ast import Num

def Solution(num):
    return len(bin(num)[2:])-1
#     test = int(math.sqrt(num))
#     if test%2 == 0:
#         test = test - 2
#     else:
#         test = test - 1
#     return 2**test
    
    
#     num = num - 1
#     while num:
#         if num & num-1 == 0:
#             return num
#         else:
#             num = num - 1
#     test = num - 1
#     result = int(math.sqrt(test))
#     while test != int(math.pow(result,2)):
#         test = test - 1
#         result = int(math.sqrt(test))
#     return test
#     num = num - 1
#     while num:
#         if num != 0 and ((num & (num - 1)) == 0) is True:
#             return num
#         else:
#             num = num - 1
#     while (num != 0 and ((num & (num - 1)) == 0)) is True:
#         num = num - 1
print(Solution(127))