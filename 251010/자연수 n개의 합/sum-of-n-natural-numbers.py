s = int(input())
left, right = 1, s
while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        left = mid + 1
    else:
        right = mid - 1

print(right)

