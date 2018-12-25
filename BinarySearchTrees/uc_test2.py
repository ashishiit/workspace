'''
Created on Jun 20, 2018

@author: S528358
'''
def String_Solution(string_list, n):
    temp = {}
    for i in string_list:
        if i not in temp:
            temp[i] = string_list.count(i)
    result = []
    for i in temp:
        if temp[i] == n:
            result.append(i)
    return result
string_list = ['red', 'red', 'blue', 'yellow', 'blue']
n = 2
print(String_Solution(string_list, n))