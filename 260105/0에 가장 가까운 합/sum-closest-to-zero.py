n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right, min_diff = 0, n - 1, 2 * 10 ** 9
while left < right:
    cur = arr[left] + arr[right]
    if abs(cur) < min_diff:
        min_diff = abs(cur)
    if cur > 0:
        right -= 1
    else:
        left += 1
print(min_diff)


