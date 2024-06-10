n = int(input())
arr = list(map(int, input().split()))
minus = 0
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[i] - arr[j] > minus:
            minus = arr[i] - arr[j]
print(minus)