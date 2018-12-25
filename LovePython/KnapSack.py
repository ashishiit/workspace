def dpKnapSack(items, W):
    n = len(items)
    T = []
    for i in range(n):
        T.append([0]*(W+1))
    for j in range(1, W + 1):
        if items[0][0] <= j:
            T[0][j] = items[0][1]
        else:
            T[0].append(T[0][0])
    for i in range(1, n):
        for j in range(1, W + 1):
            if items[i][0] <= j:
                T[i][j] = max(T[i-1][j], items[i][1] + T[i-1][j-items[i][0]])
            else:
                T[i][j] = T[i - 1][j]
    return  T[n-1][W]
def greedySolution_1(items, W):
    '''sort by weight in increasing order'''
    items = sorted(items, key = lambda test:test[0])
    n = len(items)
    w = 0
    v = 0
    for i in range(n):
        if w+items[i][0] <= W:            
            w = w + items[i][0]
            v = v + items[i][1]
    return v
def greedySolution_2(items, W):
    '''sort by value to weight ratio in decreasing order'''
    v = 0
    w = 0
    n = len(items)
    for i in range(n):
        items[i].append(items[i][1]/items[i][0])
    items = sorted(items, key = lambda test:test[2], reverse=True)
    for i in range(n):
        if w+items[i][0] <= W:
            w = w + items[i][0]
            v = v + items[i][1]
    return v
def recKnapSack(items, W):
    n = len(items)
    if W == 0:
        return 0
    if len(items) == 0:
        return 0
    if items[n-1][0] > W:
        return recKnapSack(items[:-1], W)
    else:
        return max(recKnapSack(items[:-1], W),items[n-1][1] + recKnapSack(items[:-1], W-items[n-1][0]))
    
# print(dpKnapSack(items, W))
# print(greedySolution_1(items, W))
# print(greedySolution_2(items, W))
# print(recKnapSack(items, W))