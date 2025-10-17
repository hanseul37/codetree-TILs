import heapq

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(arr, num)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)

