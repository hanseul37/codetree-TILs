m = int(input())
a, b = map(int, input().split())
min_cnt, max_cnt = m, 0
for i in range(a, b + 1):
    left, right, cnt = 1, m, 1
    while left <= right:
        mid = (left + right) // 2
        if mid == i:
            min_cnt = min(cnt, min_cnt)
            max_cnt = max(cnt, max_cnt)
            break
        if mid > i:
            right = mid - 1
        else:
            left = mid + 1
        cnt += 1
print(min_cnt, max_cnt)
