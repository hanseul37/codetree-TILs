n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_cnt, cnt = sum(arr[:k]), sum(arr[:k])
for i in range(1, n - k + 1):
    cnt = cnt + arr[i + k - 1] - arr[i - 1]
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
