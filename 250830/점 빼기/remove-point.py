from sortedcontainers import SortedSet

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
s = SortedSet(points)

for _ in range(m):
    q = int(input())
    if s.bisect_left((q, 0)) < len(s):
        print(*s[s.bisect_left((q, 0))])
        s.remove(s[s.bisect_left((q, 0))])
    else:
        print(-1, -1)
