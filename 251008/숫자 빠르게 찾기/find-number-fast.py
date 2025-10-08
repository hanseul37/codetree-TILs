n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    num = int(input())
    idx = -1
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            idx = mid + 1
            break
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    print(idx)