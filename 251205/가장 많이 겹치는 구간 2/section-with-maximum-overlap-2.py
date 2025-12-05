n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
events = []
for s, e in arr:
    events.append([s, 1])
    events.append([e, -1])
events.sort()

cnt, max_interval = 0, 0
for _, v in events:
    cnt += v
    max_interval = max(max_interval, cnt)
print(max_interval)
