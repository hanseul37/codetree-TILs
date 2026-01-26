import heapq

c, n = map(int, input().split())
t = [int(input()) for _ in range(c)]
ab = [list(map(int, input().split())) for _ in range(n)]
t.sort()
ab.sort()
cnt, idx, pq = 0, 0, []
for red in t:
    while idx < n and ab[idx][0] <= red:
        heapq.heappush(pq, ab[idx][1])
        idx += 1

    while pq and pq[0] < red:
        heapq.heappop(pq)

    if pq:
        heapq.heappop(pq)
        cnt += 1
print(cnt)
