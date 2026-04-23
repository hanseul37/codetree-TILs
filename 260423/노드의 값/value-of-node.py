import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
nodes = list(map(int, input().split()))
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

cnt = 0
def dfs(node, parent):
    global cnt
    remain = nodes[node] - 1
    for next_node in tree[node]:
        if next_node != parent:
            child_remain = dfs(next_node, node)
            remain += child_remain
            cnt += abs(child_remain)
    return remain

dfs(0, -1)
print(cnt)