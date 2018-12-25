'''
Created on Sep 15, 2018

@author: S528358
'''
def Solution(a, b):
    str1 = set()
    str2 = set()
    for i in a:
        str1.add(i)
    for j in b:
        str2.add(j)
    count = 0
    for i in str1:
        if i not in str2:
            count = count + 1
    print(count)

a = ['a', 'jk', 'abb', 'mn', 'abc']
b = ['bb', 'kj', 'bbc', 'op', 'def']

i = 0
j = 0
while i < len(a) and j < len(b):
    if len(a[i]) != len(b[j]):
        print(-1)
    else:
        Solution(a[i],b[j])
    i = i + 1
    j = j + 1
