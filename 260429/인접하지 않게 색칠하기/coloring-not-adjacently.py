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
dp = [[[-float('inf')] * 2 for _ in range(k + 1)] for _ in range(n)]

def dfs(node, parent):
    dp[node][0][0], dp[node][1][1] = 0, values[node]
    for next_node in tree[node]:
        if next_node != parent:
            dfs(next_node, node)
            child_dp = [[-float('inf')] * 2 for _ in range(k + 1)]
            for i in range(k + 1):
                for j in range(k - i + 1):
                    if dp[node][i][0] != -float('inf'):
                        child_dp[i + j][0] = max(dp[node][i][0] + max(dp[next_node][j]), child_dp[i + j][0])
                    if dp[node][i][1] != -float('inf'):
                        child_dp[i + j][1] = max(dp[node][i][1] + dp[next_node][j][0], child_dp[i + j][1])
            dp[node] = child_dp

dfs(0, -1)
print(max(max(dp[0][i]) for i in range(k + 1)))