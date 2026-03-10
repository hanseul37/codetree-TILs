m = int(input())
graph, nodes, node_in = dict(), set(), dict()
for _ in range(m):
    a, b = map(int, input().split())
    if a - 1 not in graph:
        graph[a - 1] = []
    graph[a - 1].append(b - 1)
    nodes.add(a - 1)
    nodes.add(b - 1)
    if b - 1 not in node_in:
        node_in[b - 1] = 0
    node_in[b - 1] += 1

def check():
    root, root_num, ans = -1, 0, 1
    if len(nodes) != len(node_in) + 1:
        return 0
    for node in nodes:
        if not node in node_in:
            root = node
            root_num += 1
        elif node_in[node] > 1:
            return 0
    if root_num != 1:
        return 0
    
    visited, q = set(), [root]
    while q:
        point = q.pop(0)
        if point in visited:
            return 0
        if point in graph:
            for next_point in graph[point]:
                q.append(next_point)
        visited.add(point)
    if len(visited) == len(nodes):
        return 1
    else:
        return 0

print(check())