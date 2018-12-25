a = [10, 3, 5, 6, 2]
left = [1]*len(a)
right = [1]*len(a)
for i in range(1,len(a)):
    left[i] = left[i-1] * a[i-1]
# print(left)
for j in range(len(a)-2, -1, -1):
    right[j] = right[j+1] * a[j+1]
# print(right)
for i in range(len(a)):
    print(left[i]*right[i], end=' ')
    
