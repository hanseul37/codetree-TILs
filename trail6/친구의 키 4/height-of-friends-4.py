from collections import deque

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
left, right, ans = 1, m, -1
while left <= right:
    mid = (left + right) // 2
    graph, in_degree = [[] for _ in range(n)], [0] * n
    for i in range(mid):
        graph[edges[i][0] - 1].append(edges[i][1] - 1)
        in_degree[edges[i][1] - 1] += 1
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    arr = []
    while q:
        node = q.popleft()
        arr.append(node)
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)    
    if len(arr) < n:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

if ans == -1:
    print("Consistent")
else:
    print(ans)
