import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []
for i in range(n):
    heapq.heappush(pq, arr[i])
    if i <= 1:
        print(-1)
    else:
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
        third = heapq.heappop(pq)
        heapq.heappush(pq, first)
        heapq.heappush(pq, second)
        heapq.heappush(pq, third)
        print(first * second * third)
