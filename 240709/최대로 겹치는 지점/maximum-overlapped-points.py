n = int(input())
arr = [0 for i in range(100)]
for _ in range(n):
    a, b = list(map(int, input().split()))
    for j in range(a, b + 1):
        arr[j] += 1

for i in range(100):
    if arr[i] == max(arr):
        print(arr[i])
        break