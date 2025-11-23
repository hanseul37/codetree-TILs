n = int(input())
arr = list(map(int, input().split()))
left, right = [0] * n, [0] * n
left[0], right[-1] = arr[0], arr[-1]
for i in range(1, n):
    left[i] = max(left[i - 1], arr[i])
    right[n - 1 - i] = max(right[n - i], arr[n - 1 - i])

max_value = 0
for i in range(2, n - 2):
    max_value = max(left[i - 2] + arr[i] + right[i + 2], max_value)
print(max_value)
    