import heapq

n = int(input())
arr = list(map(int, input().split()))
max_value, total = 0, arr[-1]
pq = [arr[-1]]
for i in range(n - 2, 0, -1):
    heapq.heappush(pq, arr[i])
    total += arr[i]
    max_value = max((total - pq[0]) / (len(pq) - 1), max_value)
print(f'{max_value:.2f}')


