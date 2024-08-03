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
    find = 0
    for i in range(len(y_arr) - 1):
        for j in range(i + 1, len(y_arr)):
            for k in range(len(x_arr)):
                a, b, c = y_arr[i], y_arr[j], x_arr[k]
                flag = 1
                for point in points:
                    if not (point[1] == a or point[1] == b or point[0] == c):
                        flag = 0
                if flag == 1:
                   find = 1
    for i in range(len(x_arr) - 1):
        for j in range(i + 1, len(x_arr)):
            for k in range(len(y_arr)):
                a, b, c = x_arr[i], x_arr[j], y_arr[k]
                flag = 1
                for point in points:
                    if not (point[0] == a or point[0] == b or point[1] == c):
                        flag = 0
                if flag == 1:
                    find = 1
    print(find)