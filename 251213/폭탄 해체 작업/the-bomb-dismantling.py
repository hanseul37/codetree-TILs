import heapq

n = int(input())
bombs = [list(map(int, input().split())) for _ in range(n)]
bombs.sort(key=lambda x:x[1])
arr = []
for point, limit in bombs:
    heapq.heappush(arr, point)
    if len(arr) > limit:
        heapq.heappop(arr)
print(sum(arr))
