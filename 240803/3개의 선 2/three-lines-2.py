n = int(input())
points = []
x_arr, y_arr = [], []

for _ in range(n):
    point = list(map(int, input().split()))
    if point[0] not in x_arr:
        x_arr.append(point[0])
    if point[1] not in y_arr:
        y_arr.append(point[1])
    points.append(point)

if len(x_arr) <= 3 or len(y_arr) <= 3:
    print(1)
else:
    flag = 0
    for i in range(len(y_arr) - 1):
        for j in range(i + 1, len(y_arr)):
            for k in range(len(x_arr)):
                for y in range(11):
                    for x in range(11):
                        if y == i or y == j or x == k:
                            flag = 1
    print(flag)