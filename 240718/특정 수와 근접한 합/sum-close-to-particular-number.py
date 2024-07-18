import sys

n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    for j in range(i + 1, n):
        sum = 0
        for k in range(n):
            if k == i or k == j:
                continue
            sum += arr[k]
        if min_diff > abs(s - sum):
            min_diff = abs(s - sum)
print(min_diff)