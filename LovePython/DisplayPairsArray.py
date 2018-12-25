'''
Created on Jul 20, 2017

@author: S528358
'''
A = [3, 1, 4, 2, 8]
B = [5, 2, 12, 8, 3]

# A = sorted(A)
# B = sorted(B)
C = A + B

# print(C)
A = sorted(A)
B = sorted(B)

i = 0
j = 0
ans = 0
while i < len(A) and j < len(B):
    if A[i] == B[j]:
        ans = A[i]+B[j]
        i = i + 1
        j = j + 1
    elif A[i] < B[j]:
        i = i + 1
    elif B[j] < A[i]:
        j = j + 1
print(ans)