n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt, right, min_part = [0] * (m + 1), 1, n
for left in range(1, n + 1):
    cnt[arr[left - 1]] -= 1
    while right <= n and 0 in cnt:
        cnt[arr[right]] += 1
        right += 1
    if 0 not in cnt:
        min_part = min(right - left, min_part)
print(min_part)