import heapq

n, a, b = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
ans = 0
for i in range(n):
    for j in range(n):
        distance = [[float('inf')] * n for _ in range(n)]
        distance[i][j] = 0
        q = [[0, i, j]]
        while q:
            dist, r, c = heapq.heappop(q)
            if dist > distance[r][c]:
                continue
            for dx, dy in zip(dxs, dys):
                ny, nx = r + dy, c + dx
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[ny][nx] == arr[r][c]:
                        weight = a
                    else:
                        weight = b
                    if distance[ny][nx] > dist + weight:
                        distance[ny][nx] = dist + weight
                        heapq.heappush(q, [distance[ny][nx], ny, nx])
        for y in range(n):
            for x in range(n):
                ans = max(distance[y][x], ans)
print(ans)