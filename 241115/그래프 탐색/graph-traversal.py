n, m = map(int, input().split())
arr =[[0] * n for _ in range(n)]
visited = [0]
cnt = 0

for _ in range(m):
    line = list(map(int, input().split()))
    arr[line[0] - 1][line[1] - 1] = 1
    arr[line[1] - 1][line[0] - 1] = 1

def dfs(v):
    global visited, cnt
    for i in range(n):
        if i not in visited and arr[v][i]:
            visited.append(i)
            cnt += 1
            dfs(i)

dfs(0)
print(cnt)