n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt, remain = [0] * (m + 1), [0] * (m + 1)
cnt_zero, remain_zero = m, 0
for i in range(1, n + 1):
    remain[arr[i]] += 1

right, min_part = 1, n + 1
for left in range(1, n + 1):
    cnt[arr[left - 1]] -= 1
    if cnt[arr[left - 1]] == 0:
        cnt_zero += 1
    remain[arr[left - 1]] += 1
    if remain[arr[left - 1]] == 1:
        remain_zero -= 1
    while right <= n and cnt_zero:
        cnt[arr[right]] += 1
        if cnt[arr[right]] == 1:
            cnt_zero -= 1
        remain[arr[right]] -= 1
        if remain[arr[right]] == 0:
            remain_zero += 1
        right += 1
    if not cnt_zero and not remain_zero:
        min_part = min(right - left, min_part)

if min_part == n + 1:
    print(-1)
else:
    print(min_part)