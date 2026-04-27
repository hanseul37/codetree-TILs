import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)
values = [int(input()) for _ in range(n)]
k = int(input())
dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

def dfs(node, parent):
    dp[node][1][1] = values[node]
    for next_node in tree[node]:
        if next_node != parent:
            dfs(next_node, node)
            for i in range(k, -1, - 1):
                for j in range(i + 1):
                    dp[node][i][0] = max(dp[node][i][0], dp[node][i - j][0] + max(dp[next_node][j]))
                    if i - j >= 1:
                        dp[node][i][1] = max(dp[node][i][1], dp[node][i - j][1] + dp[next_node][j][0])
dfs(0, -1)
print(max(max(dp[0])))