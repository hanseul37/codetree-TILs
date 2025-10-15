n, t = map(int, input().split())
track = []
for _ in range(n):
    start, speed = map(int, input().split())
    track.append([start, speed])
track.sort(reverse=True)

positions = []
for elem in track:
    positions.append(elem[0] + elem[1] * t)

last, cnt = float('inf'), 0
for elem in positions:
    if last > elem:
        cnt += 1
        last = elem

print(cnt)


