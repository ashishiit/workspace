N = int(input())
a = [int(i) for i in input().split(' ')]
def Swap(left, right):
    temp = a[right]
    a[right] = a[left]
    a[left] = temp
left = 0
right = len(a) - 1
while left < right:
    Swap(left,right)
    left = left + 1
    right = right - 1
print(a)
