import heapq

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(arr, -num)
    else:
        if not arr:
            print(0)
        else:
            print(-heapq.heappop(arr))



