arr = list(map(int, input().split()))
arr.sort()
print(arr[0], end=' ')
print(arr[1], end=' ')
print(arr[2], end=' ')
print(arr[-1] - arr[0] - arr[1] - arr[2])