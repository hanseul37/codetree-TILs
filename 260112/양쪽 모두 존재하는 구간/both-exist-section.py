n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt, right, min_part = [0] * (m + 1), 1, n + 1
for left in range(1, n + 1):
    cnt[arr[left - 1]] -= 1
    while right <= n and 0 in cnt:
        cnt[arr[right]] += 1
        right += 1
    if 0 not in cnt:
        min_part = min(right - left, min_part)
if min_part == n + 1:
    print(-1)
else:
    print(min_part)