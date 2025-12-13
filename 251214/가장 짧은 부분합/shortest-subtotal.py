n, s = map(int, input().split())
arr = list(map(int, input().split()))
min_cnt, total, j = n, 0, 0
for i in range(n):
    while j < n and total < s:
        total += arr[j]
        j += 1
    min_cnt = min(j - i + 1, min_cnt)
    total -= arr[i]
print(min_cnt)
