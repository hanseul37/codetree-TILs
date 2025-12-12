from sortedcontainers import SortedList

n = int(input())
arr = []
for i in range(n):
    y, x1, x2 = map(int, input().split())
    arr.append([x1, y, i, 1])
    arr.append([x2, y, i, -1])
arr.sort()

cnt = 0
color = SortedList()
for x, y, idx, v in arr:
    if v == 1:
        color.add((y, idx))
        if color[0][1] == idx:
            cnt += 1
    else:
        if len(color) > 1 and color[0][1] == idx:
            cnt += 1
        color.remove((y, idx))
print(cnt)

