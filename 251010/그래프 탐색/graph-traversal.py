n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
visited = [False] * n
visited[0] = True
cnt = 0

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1 - 1][v2 - 1] = True
    graph[v2 - 1][v1 - 1] = True

def dfs(vertex):
    global cnt
    for i in range(n):
        if graph[vertex][i] == True and not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)

dfs(0)
print(cnt)