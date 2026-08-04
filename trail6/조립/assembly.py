from collections import deque

n, m = map(int, input().split())
graph, in_degree, dp = [[] for _ in range(n)], [0] * n, [0] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])
    in_degree[b - 1] += 1

q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

dp[n - 1] = 1
while q:
    node = q.popleft()
    for next_node, cnt in graph[node]:
        dp[next_node] += dp[node] * cnt
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
        
for i in range(n):
    if not graph[i] and dp[i]:
        print(i + 1, dp[i])
