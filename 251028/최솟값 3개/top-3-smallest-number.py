import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []
first, second = -1, -1
for i in range(n):
    if i <= 1:
        print(-1)
        if i == 1:
            first = min(arr[0], arr[1])
            second = max(arr[0], arr[1])
    else:
        if second > arr[i]:
            heapq.heappush(pq, second)
            second = arr[i]
        else:
            heapq.heappush(pq, arr[i])
        print(first * second * pq[0])


