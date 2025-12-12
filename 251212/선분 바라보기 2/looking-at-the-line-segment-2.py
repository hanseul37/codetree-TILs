from sortedcontainers import SortedList

n = int(input())
arr = []
for i in range(n):
    y, x1, x2 = map(int, input().split())
    arr.append([x1, y, i, 1])
    arr.append([x2, y, i, -1])
arr.sort()

lowest = set()
color = SortedList()
for x, y, idx, v in arr:
    before = color[0][1] if len(color) > 0 else -1
    if v == 1:
        color.add((y, idx))
    else:
        color.remove((y, idx))
    after = color[0][1] if len(color) > 0 else -1

    if after != before and after != -1:
        lowest.add(after)

print(len(lowest))

