n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
cnt, left, right = 0, 0, n - 1
while left < right:
    if arr[left] + arr[right] <= k:
        cnt += right - left
        left += 1
    else:
        right -= 1
print(cnt) 


