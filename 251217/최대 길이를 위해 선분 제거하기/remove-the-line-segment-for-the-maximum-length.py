n = int(input())
arr = []
for i in range(n):
    x1, x2 = map(int, input().split())
    arr.append([x1, i, 1])
    arr.append([x2, i, -1])
arr.sort()

active, unique, prev, total = set(), [0] * n, arr[0][0], 0
for location, point, v in arr:
    interval = location - prev
    if interval > 0:
        if len(active) > 0:
            total += interval
        if len(active) == 1:
            (active_id, ) = active
            unique[active_id] += interval
    if v == 1:
        active.add(point)
    else:
        if point in active:
            active.remove(point)
    prev = location
print(total - min(unique))
    

