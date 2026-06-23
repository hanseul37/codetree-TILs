n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    if arr[v1 - 1][v2 - 1]:
        arr[v1 - 1][v2 - 1] = min(arr[v1 - 1][v2 - 1], weight)
    else:
        arr[v1 - 1][v2 - 1] = weight
    if arr[v2 - 1][v1 - 1]:
        arr[v2 - 1][v1 - 1] = min(arr[v2 - 1][v1 - 1], weight)
    else:
        arr[v2 - 1][v1 - 1] = weight

dist, visited = [float('inf')] * n, [False] * n
dist[0], ans = 0, 0
for i in range(n):
    min_idx = -1
    for j in range(n):
        if not visited[j]:
            if min_idx == -1 or dist[min_idx] > dist[j]:
                min_idx = j
    visited[min_idx] = True
    ans += dist[min_idx]
    for j in range(n):
        if arr[min_idx][j] != 0:
            dist[j] = min(arr[min_idx][j], dist[j])
print(ans)