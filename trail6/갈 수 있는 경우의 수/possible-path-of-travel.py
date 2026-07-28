from collections import deque

n, m = map(int, input().split())
graph, in_degree, dp = [[] for _ in range(n)], [0] * n, [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    in_degree[y - 1] += 1
dp[0] = 1

q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    for next_node in graph[node]:
        dp[next_node] += dp[node]
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
print(dp[-1] % 1000000007)