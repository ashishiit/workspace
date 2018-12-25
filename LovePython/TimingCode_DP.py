import random
from KnapSack import dpKnapSack,greedySolution_1, greedySolution_2, recKnapSack
from time import perf_counter
W = 100
iter = 100
n = int(input('n = '))
items = []
for i in range(n):
    items.append([random.randrange(1,W) , random.randrange(1,100)])

def timefuncs(n, W, iter):
    dpTime = 0
    greedyTime_1 = 0
    greedyTime_2 = 0
    recTime = 0
    avgQuality_1 = 0
    avgQuality_2 = 0
    for i in range(iter):
        '''time : sort by weight in increasing order'''
        start = perf_counter()
        gsoln_1 = greedySolution_1(items, W)
        end = perf_counter()
        greedyTime_1 += (end-start)/float(iter)
        '''time : value to weight ration, sorted in decreasing order'''
        start = perf_counter()
        gsoln_2 = greedySolution_2(items, W)
        end = perf_counter()
        greedyTime_2 += (end-start)/float(iter)
        ''' time : dp solution'''
        start = perf_counter()
        dpsoln = dpKnapSack(items, W)
        end = perf_counter()
        dpTime += (end-start)/float(iter)
        '''time : recursive solution. PLEASE COMMENT loc 35-38 while comparing other algorithms.
        Run the timing code for recursion separately because it takes lot of time to execute'''
        start = perf_counter()
        recsoln = recKnapSack(items, W)
        end = perf_counter()
        recTime += (end-start)/float(iter)
        '''comparing the quality of the algorithms'''
        avgQuality_1 += (float(gsoln_1)/float(dpsoln))/iter
        avgQuality_2 += (float(gsoln_2)/float(dpsoln))/iter
        '''Please delete recTime from loc 43 while comparing other algorithms'''
    return greedyTime_1, greedyTime_2, dpTime, avgQuality_1, avgQuality_2, recTime

print(timefuncs(n, W, iter))