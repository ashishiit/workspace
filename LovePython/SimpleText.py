'''
Created on Apr 21, 2017

@author: S528358
'''
# txt= 'Google'
inp = open('input.txt','r+')
pat = input('enter pattern')
result = []
count = 0
for a in inp:
#     print(a)
    for i in range(len(a)):
        for j in range(len(pat)):
            if a[i + j] != pat[j]:
                count = count + 1
                break
        if j == len(pat) - 1:
            result.append(i)
print(max(result))
print(count+1)
