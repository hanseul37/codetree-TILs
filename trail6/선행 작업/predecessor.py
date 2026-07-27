from collections import deque

n = int(input())
graph, in_degree, arr, dp = [[] for _ in range(n)], [0] * n, [], [0] * n 
for i in range(n):
    cost, _, *works = map(int, input().split())
    for w in works:
        graph[w - 1].append(i) 
        in_degree[i] += 1
    arr.append(cost)
    dp[i] = cost

q = deque() 
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    for next_node in graph[node]:
        dp[next_node] = max(dp[next_node], dp[node] + arr[next_node])
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
print(max(dp))