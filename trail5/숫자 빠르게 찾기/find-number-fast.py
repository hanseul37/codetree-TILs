n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    num = int(input())
    left, right, ans = 0, n - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            ans = mid + 1
            break
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
