n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    num = int(input())
    left, right = 0, n - 1
    min_idx, max_idx = n, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= num:
            right = mid - 1
        else:
            left = mid + 1
    min_idx = left

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= num:
            left = mid + 1
        else:
            right = mid - 1
    max_idx = left
    print(max_idx - min_idx)
