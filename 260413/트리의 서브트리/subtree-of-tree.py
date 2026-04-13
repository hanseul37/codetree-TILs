n, r, q = map(int, input().split())
tree, cnt = [[] for _ in range(n + 1)], [0] * (n + 1)
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

visited = [False] * (n + 1)
visited[r] = True
def dfs(node):
    cnt[node] = 1
    for child in tree[node]:
        if not visited[child]:
            visited[child] = True
            dfs(child)
            cnt[node] += cnt[child]

dfs(r)
for _ in range(q):
    u = int(input())
    print(cnt[u])
