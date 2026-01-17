n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, cnt, min_len = 0, 0, n + 1
for right in range(n):
    if arr[right] == 1:
        cnt += 1
    while cnt >= k:
        min_len = min(right - left + 1, min_len)
        if arr[left] == 1:
            cnt -= 1
        left += 1

print(min_len if min_len != n + 1 else -1)
