import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
pq = [[arr1[0] + arr2[0], 0, 0]]

for _ in range(k):
    value, i, j = heapq.heappop(pq)

    if i + 

    


