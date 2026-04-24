n = int(input())
tree, values = [[] for _ in range(n + 1)], [0] * (n + 1)
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
for i in range(n):
    values[i + 1] = int(input())
ans = -float('inf')

def dfs(node, parent):
    global ans
    child = []
    for next_node in tree[node]:
        if next_node != parent:
            child.append(dfs(next_node, node))
    child.sort(reverse=True)
    if child and child[0] > 0:
        max_child = values[node] + child[0]
    else:
        max_child = values[node]
    current = values[node]
    if len(child) >= 1 and child[0] > 0:
        current += child[0]
    if len(child) >= 2 and child[1] > 0:
        current += child[1]
    ans = max(ans, current, max_child)
    return max_child

dfs(1, 0)
print(ans)
    
