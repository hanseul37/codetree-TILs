s = int(input())
left, right = 1, s
while left <= right:
    mid = (left + right) // 2
    if (mid + 1) * mid / 2 > s:
        right = mid - 1
    else:
        left = mid + 1
print(right)