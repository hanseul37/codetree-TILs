n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1 
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
