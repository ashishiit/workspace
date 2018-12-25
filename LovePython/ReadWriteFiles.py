'''
Created on Apr 21, 2017

@author: S528358
'''
inp = open('input.txt', 'r+')
out = open('output.txt', 'r+')
for i in inp:
    out.write(i)
inp.close()
out.close()