n, d = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()
left, min_range = 0, 1000001
min_q, max_q = [], []
for right in range(n):
    while min_q and min_q[-1] > points[right][1]:
        min_q.pop()
    min_q.append(points[right][1])
    while max_q and max_q[-1] < points[right][1]:
        max_q.pop()
    max_q.append(points[right][1])
    
    while max_q[0] - min_q[0] >= d:
        min_range = min(points[right][0] - points[left][0], min_range)
        if min_q[0] == points[left][1]:
            min_q.pop(0)
        if max_q[0] == points[left][1]:
            max_q.pop(0)
        left += 1
if min_range == 1000001:
    print(-1)
else:
    print(min_range)
