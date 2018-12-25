inp = open('input.txt','r+')
pat = input('enter pattern')
result = []
# count = 0

    
def SimpleSearch(a):
    result = []
    count = 0
    for i in range(len(a)):
        for j in range(len(pat)):
            if a[i + j] != pat[j]:
                count = count + 1
                break
        if j == len(pat) - 1:
            result.append(i)
    print('first occurrence of pattern = ',max(result))
    print('number of comparisons = ',count+1)
def BoyerMooreHorspool(pattern, text):
    count = 0
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
            count = count + 1
        if j == -1: print('first occurrence of pattern = ', i + 1)
        k += skip[ord(text[k])]
    print('number of comparisons = ',count)


for a in inp:
    test = a
    SimpleSearch(test)
    print('*****************BMH results below this line***************')
#     print(test)
    BoyerMooreHorspool(pat, test)