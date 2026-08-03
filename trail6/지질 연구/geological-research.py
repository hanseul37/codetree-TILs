from collections import deque

n, m = map(int, input().split())
graph, in_degree, dp = [[] for _ in range(n)], [0] * n, [0] * n
for _ in range(m):
    s, e = map(int, input().split())
    graph[s - 1].append(e - 1)
    in_degree[e - 1] += 1

max_p, q = [[0, 0] for _ in range(n)], deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)
        dp[i] = 1
        
while q:
    node = q.popleft()
    for next_node in graph[node]:
        if dp[node] > max_p[next_node][0]:
            max_p[next_node] = [dp[node], 1]
        elif dp[node] == max_p[next_node][0]:
            max_p[next_node][1] += 1
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            dp[next_node] = max_p[next_node][0]
            if max_p[next_node][1] >= 2:
                dp[next_node] += 1
            q.append(next_node)

print(max(dp))