import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []
for elem in arr:
    heapq.heappush(pq, -elem)

while len(pq) >= 2:
    num1 = -heapq.heappop(pq)
    num2 = -heapq.heappop(pq)
    heapq.heappush(pq, -(num1 - num2))

if pq:
    print(-heapq.heappop(pq))
else:
    print(-1)

