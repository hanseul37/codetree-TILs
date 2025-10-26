import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
pq = [[arr1[0] + arr2[0], 0, 0]]
visited = {(0, 0)}

for _ in range(k):
    value, i, j = heapq.heappop(pq)
    if i + 1 < n and (i + 1, j) not in visited:
        heapq.heappush(pq, [arr1[i + 1] + arr2[j], i + 1, j])
        visited.add((i + 1, j))
    if j + 1 < m and (i, j + 1) not in visited:
        heapq.heappush(pq, [arr1[i] + arr2[j + 1], i, j + 1])
        visited.add((i, j + 1))

print(value)
