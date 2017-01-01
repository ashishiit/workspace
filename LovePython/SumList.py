'''
Created on Oct 28, 2016

@author: s528358
'''
def SumList(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        answer = num_list[0]+SumList(num_list[1:])
    return answer
print('sum = %d'%SumList([1, 3, 5, 7, 9]))