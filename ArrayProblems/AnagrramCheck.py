'''
Created on Oct 11, 2018

@author: S528358
'''
def AnagramCheck(a, b):
    temp_a = {}
    temp_b = {}
    for i in a:
        if i not in temp_a:
            temp_a[i] = 1
        else:
            temp_a[i] = temp_a[i] + 1
    for i in b:
        if i not in temp_b:
            temp_b[i] = 1
        else:
            temp_b[i] = temp_b[i] + 1
#     print('first = ', temp_a)
#     print('second = ', temp_b)
    
    if temp_a == temp_b:
        print('it is anagram')
    else:
        print('NOT anagram')
a = 'SILENTS'
b = 'LISTEN'

AnagramCheck(a,b)