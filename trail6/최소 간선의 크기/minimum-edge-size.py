n, m = map(int, input().split())
a, b = map(int, input().split())
arr = [int(i) for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        arr[root_x] = root_y

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2], reverse=True)

ans = 0
for v1, v2, weight in edges:
    union(v1, v2)
    if find(a) == find(b):
        ans = weight
        break
print(ans)