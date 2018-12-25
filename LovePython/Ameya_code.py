'''
Created on Jul 28, 2017

@author: S528358
'''
def toAndFro(a, b, t):
    len = abs(b - a)
    t %= 2 * len
    if t <= len:
        return a + (b-a)/abs(b-a)*t
    #else:
        
print(toAndFro(2, 4, 9))