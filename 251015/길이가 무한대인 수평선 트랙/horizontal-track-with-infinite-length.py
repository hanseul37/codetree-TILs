from sortedcontainers import SortedList
n, t = map(int, input().split())
track = SortedList(key=lambda x: (-x[0], x[1]))
for _ in range(n):
    start, speed = map(int, input().split())
    track.add([start, speed])

for _ in range(t):
    last_location, last_speed = 10 ** 9 + 1, 0   
    for elem in track:
        if elem[0] + elem[1] >= last_location:
            elem[0] = last_location
            elem[1] = last_speed
        else:
            elem[0] += elem[1]
            last_location = elem[0]
            last_speed = elem[1]

cnt, point = 0, 0
for location, _ in track:
    if location != point:
        cnt += 1
        point = location

print(cnt)

