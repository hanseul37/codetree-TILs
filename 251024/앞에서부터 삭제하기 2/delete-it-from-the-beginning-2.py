import heapq

n = int(input())
arr = list(map(int, input().split()))
max_value = 0
for i in range(1, n - 1):
    temp = arr[i:]
    heapq.heapify(temp)
    heapq.heappop(temp)
    max_value = max(sum(temp) / len(temp), max_value)
print(f'{max_value:.2f}')


