import heapq 

n, m = map(int, input().split())
a, b, warning = [[] for _ in range(n)], [[] for _ in range(n)], [[] for _ in range(n)]  
ra, rb = [[] for _ in range(n)], [[] for _ in range(n)]  # 🔥 역그래프 추가

for _ in range(m):
    v1, v2, aw, bw = map(int, input().split())
    u = v1 - 1
    v = v2 - 1

    a[u].append([v, aw])
    b[u].append([v, bw])
    warning[u].append([v, 2])

    ra[v].append([u, aw])  # 🔥 역방향 저장
    rb[v].append([u, bw])

def dijkstra(graph, start):
    distance = [float('inf')] * n
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next_node, weight in graph[node]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance

# 1️⃣ 시작점 기준
dist_a = dijkstra(a, 0)
dist_b = dijkstra(b, 0)

# 2️⃣ 도착점(N-1) 기준 역그래프
dist_a_rev = dijkstra(ra, n-1)
dist_b_rev = dijkstra(rb, n-1)

# 3️⃣ 간선이 1→N 최단경로 위에 있는지 검사
for i in range(n):
    for j in range(len(warning[i])):
        v = a[i][j][0]
        aw = a[i][j][1]
        bw = b[i][j][1]

        # A 기준
        if not (dist_a[i] + aw + dist_a_rev[v] == dist_a[n-1]):
            warning[i][j][1] -= 1

        # B 기준
        if not (dist_b[i] + bw + dist_b_rev[v] == dist_b[n-1]):
            warning[i][j][1] -= 1

# 4️⃣ 경고 그래프 다익스트라
dist_warning = dijkstra(warning, 0)
print(dist_warning[n-1])