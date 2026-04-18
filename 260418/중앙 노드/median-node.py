import sys
sys.setrecursionlimit(10**6)

n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

dp = [0] * (n + 1)
visited = [False] * (n + 1)

# subtree 크기 계산
def dfs(node):
    visited[node] = True
    dp[node] = 1
    for nxt in tree[node]:
        if not visited[nxt]:
            dfs(nxt)
            dp[node] += dp[nxt]

dfs(r)

# center 찾기 (루트부터 내려가면서)
visited = [False] * (n + 1)

def find_center(node):
    visited[node] = True
    children = []

    for nxt in tree[node]:
        if not visited[nxt]:
            children.append(nxt)

    # 조건: 자식 2개 이상
    if len(children) >= 2:
        return node

    # 자식 없으면 (리프)
    if not children:
        return node

    # 자식 1개면 계속 내려감
    return find_center(children[0])

center = find_center(r)

# 결과 계산
children_sizes = []
visited = [False] * (n + 1)
visited[center] = True

for nxt in tree[center]:
    if not visited[nxt]:
        children_sizes.append(dp[nxt])

print(max(children_sizes) - min(children_sizes))