n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(x, y):
    visited[y][x] = 1
    cnt = 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
    
        if 0 <= new_x < n and 0 <= new_y < n and visited[new_y][new_x] == 0 and arr[new_y][new_x] == 1:
            cnt += dfs(new_x, new_y)

    return cnt

villages = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            villages.append(dfs(j, i))

villages.sort()
print(len(villages))
for elem in villages:
    print(elem)