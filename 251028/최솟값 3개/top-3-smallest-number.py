import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []
for i in range(n):
    heapq.heappush(pq, arr[i])
    if i <= 1:
        print(-1)
    else:
        ans = 1
        arr_copy = arr[:i + 1]
        for _ in range(3):
            ans *= heapq.heappop(arr_copy)
        print(ans)


