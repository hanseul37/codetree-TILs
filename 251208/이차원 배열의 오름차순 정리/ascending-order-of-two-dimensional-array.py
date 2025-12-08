n = int(input())
k = int(input())
left, right = 0, n * n - 1
while left < right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    if cnt >= k:
        right = mid
    else:
        left = mid + 1
print(left)