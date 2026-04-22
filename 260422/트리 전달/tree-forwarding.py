n, m = map(int, input().split())
tree, weight = [[] for _ in range(n + 1)], [0] * (n + 1)
parent = list(map(int, input().split()))

for i in range(1, n):
    tree[parent[i]].append(i + 1)

for _ in range(m):
    i, w = map(int, input().split())
    weight[i] += w

for i in range(1, n):
    weight[i + 1] += weight[parent[i]]

print(*weight[1:])