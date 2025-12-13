n, m = map(int, input().split())
points = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(m)]

def lower(num):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if points[mid] >= num:
            right = mid - 1
        else:
            left = mid + 1
    return left

def upper(num):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if points[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return left

for start, end in lines:
    print(upper(end) - lower(start))

