import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)

for _ in range(m):
    temp = pq[0] + 1
    heapq.heappop(pq)
    heapq.heappush(pq, temp)

print(-pq[0])