'''
Created on Oct 27, 2016

@author: s528358
'''
import re
import itertools
def getAnagramIndices(haystack, needle):
    # WRITE YOUR CODE HERE
    a = []
    test = ["".join(perm) for perm in itertools.permutations(needle)]
    for i in test:
        a = a + [n for n in range(len(haystack)) if haystack.find(i,n) == n]
    a.sort()
    return a