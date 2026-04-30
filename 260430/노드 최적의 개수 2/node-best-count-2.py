import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
tree, dp = [[] for _ in range(n + 1)], [[0] * 2 for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
objects = set(map(int, input().split()))

def dfs(node, parent):
    if node in objects:
        dp[node][0] = float('inf')
    else:
        dp[node][1] = 1
    for next_node in tree[node]:
        if next_node != parent:
            dfs(next_node, node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node][0], dp[next_node][1])

dfs(1, 0)
print(min(dp[1][0], dp[1][1]))
