n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    num = int(input())
    left, right = 0, n - 1
    min_idx, max_idx = n, -1
    while left <= right:
        mid (left + right) // 2
        if arr[mid] > num:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            max_idx = max(max_idx, mid)
            left = mid + 1
    print(max_idx - min_idx)
