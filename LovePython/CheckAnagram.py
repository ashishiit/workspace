'''
Created on Sep 30, 2016

@author: S528358
'''
s1 = 'heart'
s2 = 'earthh'
s1_count = [0]*26
s2_count = [0]*26
for i  in s1:
    s1_count[ord(i)-ord('a')] = s1_count[ord(i)-ord('a')] + 1
for i in s2:
    s2_count[ord(i)-ord('a')] = s2_count[ord(i)-ord('a')] + 1
if s1_count == s2_count:
    print('anagram')
else:
    print('sorry!! not anagram')