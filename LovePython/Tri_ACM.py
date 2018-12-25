'''
Created on Apr 4, 2017

@author: S528358
'''
a = [int(i) for i in input().split(' ')]
if (a[2]-a[1]==a[0]):
    print(a[0],'+',a[1],'=',a[2])

if a[1]>a[0] and a[2]>a[1]:
    print(a[0],'=',a[1],'/',a[2])
    
if a[1]+a[2] == a[0]:
    print(a[0],'-',a[1],'=',a[2])
    
if a[0]*a[1] == a[2]:
    print(a[2],'/',a[1],'=',a[0])

if a[1]*a[2] == a[0]:
    print(a[0],'/',a[1],'=',a[2])
    
if a[2]>=a[1] and a[2]>=0:
    print(a[0],'*',a[1],'=',a[2])
    
    
