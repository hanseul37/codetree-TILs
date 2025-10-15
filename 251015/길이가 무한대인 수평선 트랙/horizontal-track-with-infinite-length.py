n, t = map(int, input().split())
track = [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    last_location = float('inf')
    new_track = []
    # 뒤에서부터 순회
    for start, speed in reversed(track):
        if start + speed < last_location:
            new_track.append([start + speed, speed])
            last_location = start + speed
    track = list(reversed(new_track))  # 다시 원래 순서로

print(len(track))
