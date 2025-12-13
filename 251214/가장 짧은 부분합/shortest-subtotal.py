n, s = map(int, input().split())
arr = list(map(int, input().split()))
min_cnt, total, j = n, 0, 0
for i in range(n):
    while j < n and total < s:
        total += arr[j]
        j += 1
    if total >= s:
        min_cnt = min(j - i, min_cnt)
    total -= arr[i]
if min_cnt == n:
    print(-1)
else:
    print(min_cnt)
