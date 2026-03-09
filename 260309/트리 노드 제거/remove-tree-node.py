n = int(input())
parent = list(map(int, input().split()))
remove = int(input())
tree = [[] for _ in range(n)]
root = -1
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]].append(i)

def dfs(node):
    if node == remove:
        return 0
    cnt, leaf = 0, True
    for next_node in tree[node]:
        if next_node != remove:
            cnt += dfs(next_node)
            leaf = False
    if leaf:
        return 1
    return cnt

print(dfs(root))

