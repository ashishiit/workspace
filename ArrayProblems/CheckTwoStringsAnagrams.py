'''
Created on Sep 15, 2018

@author: S528358
'''
def Solution(str1, str2):
    str1_dict = {}
    str2_dict = {}
    for i in str1:
        if i not in str1_dict:
            str1_dict[i] = 0
        else:
            str1_dict[i] = str1_dict[i] + 1
    for j in str2:
        if j not in str2_dict:
            str2_dict[j] = 0
        else:
            str2_dict[j] = str2_dict[j] + 1
    if str1_dict == str2_dict:
        print('anagram!!')
    else:
        print('not anagram')
        
Solution('abc','abcc')