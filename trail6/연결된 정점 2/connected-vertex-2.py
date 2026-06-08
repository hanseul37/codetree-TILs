import sys
input = sys.stdin.readline

n = int(input())
parent, size = dict(), dict()

def find(x):
    if x not in parent:
        parent[x] = x
        size[x] = 1
        return x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x == root_y:
        return size[root_x]
    parent[root_x] = root_y
    size[root_y] += size[root_x]
    return size[root_y]

for _ in range(n):
    a, b = map(int, input().split())
    print(union(a, b))