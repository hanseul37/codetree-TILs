n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
left, right = [0] * n, [0] * n
for i in range(1, n):
    left[i] = left[i - 1] + abs(arr[i][0] - arr[i - 1][0]) + abs(arr[i][1] - arr[i - 1][1])
    right[n - i - 1] = right[n - i] + abs(arr[n - i - 1][0] - arr[n - i][0]) + abs(arr[n - i - 1][1] - arr[n - i][1])

min_dist = float('inf')
for i in range(1, n - 1):
    min_dist = min(min_dist, left[i - 1] + right[i + 1] + abs(arr[i - 1][0] - arr[i + 1][0]) + abs(arr[i - 1][1] - arr[i + 1][1]))

print(min_dist)
