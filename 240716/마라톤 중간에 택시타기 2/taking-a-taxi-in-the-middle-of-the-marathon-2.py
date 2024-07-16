import sys

n = int(input())
arr = []
for _ in range(n):
    point = list(map(int, input().split()))
    arr.append(point)

min = sys.maxsize
for i in range(1, n - 1):
    sum = 0
    last_x, last_y = arr[0][0], arr[0][1]
    for j in range(1, n):
        if j == i:
            continue
        sum += (abs(arr[j][0] - last_x) + abs(arr[j][1] - last_y))
        last_x = arr[j][0]
        last_y = arr[j][1]

    if sum < min:
        min = sum

print(min)