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
        min3 = heapq.nsmallest(3, pq)
        for elem in min3:
            ans *= elem
        print(ans)


