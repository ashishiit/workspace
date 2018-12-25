def Insertion_Sort(a,n = None):
    for i in range(1, len(a)):
        temp = a[i]
        j = i
        while j > 0 and temp < a[j-1]:
            a[j] = a[j-1]
            j = j - 1
            a[j] = temp
    return a
def QuickSort_Sort(a, left, right,n = None):
    if left < right:
        pivot = Partition(a, left, right)
        QuickSort_Sort(a, left, pivot-1)
        QuickSort_Sort(a, pivot+1, right)
    return a
def Builtin_Sort(a):
    return sorted(a)
def Select_Algo(a, left, right, k):
    pivot = Partition(a, left, right)
    if pivot == k:
        return a[pivot]
    elif pivot > k:
        return Select_Algo(a, left, pivot-1,k)
    else:
        return Select_Algo(a, pivot+1, right,k)    
def Partition(a, leftPtr, rightPtr):
    left = leftPtr
    right = rightPtr - 1
    pivot = a[rightPtr]
    while True:
        while a[left] < pivot:
            left = left + 1
        while a[right] > pivot:
            right = right - 1
        if left < right:
            Swap(a, left, right)
        else:
            break
    Swap(a,left,rightPtr)
    return left
def Swap(a, left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp