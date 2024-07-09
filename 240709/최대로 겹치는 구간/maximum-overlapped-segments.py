n = int(input())
arr = [0 for i in range(200)]
for i in range(n):
    a, b = list(map(int, input().split()))
    for j in range(a, b):
        arr[j + 100] += 1

cnt = 0
for i in range(200):
    if arr[i] == max(arr):
        print(arr[i])
        break