import random
from Main_Solution import Insertion_Sort, QuickSort_Sort, Select_Algo
from time import perf_counter
N = 20000
ITERS = 1000
k = int(input('k ='))
L = random.sample(range(1,101),100)
def Timing_Test_QuickSort(L):    
    elapsed_quicksort = 0
    for i in range(ITERS):
        start_quicksort = perf_counter()
        QuickSort_Sort(L, 0, len(L)-1,N//2)
        end_quicksort = perf_counter()
        elapsed_quicksort += (end_quicksort - start_quicksort)
    print('Quicksort select:   ', elapsed_quicksort/N, 's')
def Timing_Test_SelectAlgo(L):
    elapsed_select = 0    
    for i in range(ITERS):
        start_select = perf_counter()
        #Insertion_Sort(L,N//2)
        Select_Algo(L, 0, len(L)-1, k)
        end_select = perf_counter()
        elapsed_select += (end_select - start_select)
    print('Select algorithm:   ', elapsed_select/N, 's')
def Timing_Test_InsertionSort(L):
    elapsed_insertion = 0    
    for i in range(ITERS):
        start_insertion = perf_counter()
        Insertion_Sort(L,N//2)        
        end_insertion = perf_counter()
        elapsed_insertion += (end_insertion - start_insertion)
    print('Insertion Sort:   ', elapsed_insertion/N, 's')
        
def Timing_Test_BuiltIn(L):
    elapsed_builtin = 0
    for i in range(ITERS):
        start_builtin = perf_counter()        
        L.sort()
        end_builtin = perf_counter()
        elapsed_builtin += (end_builtin - start_builtin)
    print('Builtin sort sel:   ', elapsed_builtin/N, 's')
L = random.sample(range(1,101),100)
print('-- Iterations: %d'%ITERS)
print('-- List length: %d'%N)
Timing_Test_SelectAlgo(L)
Timing_Test_QuickSort(L)
Timing_Test_BuiltIn(L)
Timing_Test_InsertionSort(L)