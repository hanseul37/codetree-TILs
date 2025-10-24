import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    left, right = [], []
    for i in range(len(arr)):
        if not left or arr[i] < -left[0]:
            heapq.heappush(left, -arr[i])
        else:
            heapq.heappush(right, arr[i])

        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(left) < len(right):
            heapq.heappush(left, -heapq.heappop(right))
            
        if i % 2 == 0:
            print(-left[0], end = ' ')
    print()


