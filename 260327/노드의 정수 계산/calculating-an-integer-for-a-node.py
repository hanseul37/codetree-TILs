n = int(input())
tree, values = [[] for _ in range(n)], [0] * n
for i in range(1, n):
    t, a, p = map(int, input().split())
    tree[p - 1].append(i)
    values[i] = a if t == 1 else -a

def dfs(node):
    for child in tree[node]:
        dfs(child)
        if values[child] > 0:
            values[node] += values[child]

dfs(0)
print(values[0])