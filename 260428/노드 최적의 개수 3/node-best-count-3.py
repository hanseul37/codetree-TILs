import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree, dp = [[] for _ in range(n)], [[0] * 3 for _ in range(n)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

def dfs(node, parent):
    dp[node], flag, diff = [0, 0, 1], False, float('inf')
    for next_node in tree[node]:
        if next_node != parent:
            dfs(next_node, node)
            dp[node][0] += min(dp[next_node][1], dp[next_node][2])
            if dp[next_node][2] <= dp[next_node][1]:
                dp[node][1] += dp[next_node][2]
                flag = True
            else:
                dp[node][1] += dp[next_node][1]
                diff = min(dp[next_node][2] - dp[next_node][1], diff)
            dp[node][2] += min(dp[next_node])
    if not flag:
        dp[node][1] += diff

dfs(0, -1)
print(min(dp[0][1], dp[0][2]))
 