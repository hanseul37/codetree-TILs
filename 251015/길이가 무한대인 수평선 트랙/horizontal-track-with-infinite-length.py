from sortedcontainers import SortedList
n, t = map(int, input().split())
track = SortedList(key=lambda x: -x[0])
for _ in range(n):
    start, speed = map(int, input().split())
    track.add([start, speed])

for _ in range(t):
    last_location, last_speed = float('inf'), 0   
    new_track = []
    for elem in track:
        if elem[0] + elem[1] < last_location:
            new_location = elem[0] + elem[1]
            new_track.append([new_location, elem[1]])
            last_location = new_location
            last_speed = elem[1]
    track = new_track

print(len(track))

