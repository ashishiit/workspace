'''
Created on Jan 7, 2017

@author: S528358
'''
import math
f = open('progress_pie.txt')
out = open('output_1.txt','r+')
T = int(f.readline().strip())
# f.readline()
temp = []

for i in range(T):
    [p,x,y] =(int(i) for i in f.readline().split(' '))
#     t = f.readline()
#     print(t)
#     print('p = %d'%p)
#     print('x = %d'%x)
#     print('y = %d'%y)
#     print('***********')
    ad = 45
    
    ap = round((p/100)*360,2)
    rp = 50
    xp = 50
    yp = 50
    xt = x - xp
    yt = y - yp
    at = math.atan2(yt,xt)
    check = math.sqrt(pow(xt,2)+pow(yt,2))
#     print('check = %d'%check)
    if check<=rp and (ad - ap)<=at:
        out.write('Case #%d: black\n'%(i+1))
    else:
        out.write('Case #%d: white\n'%(i+1))
    