n, k = map(int, input().split())
arr = list(map(int, input().split()))

point = 0
values = arr[0]

while point < n - 1:
    next_point = min(point + k, n - 1)
    min_val = min(arr[point + 1:next_point + 1])
    point = arr.index(min_val, point + 1, next_point + 1)
    values = max(values, arr[point])

print(values)