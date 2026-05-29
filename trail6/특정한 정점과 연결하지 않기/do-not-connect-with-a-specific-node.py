n, m = map(int, input().split())
arr = [int(i) for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for _ in range(m):
    v1, v2 = map(int, input().split())
    union(v1, v2)

a, b, k = map(int, input().split())
root_a, root_b, group = find(a), find(b), dict()
for i in range(1, n + 1):
    point = find(i)
    if point in group:
        group[point] += 1
    else:
        group[point] = 1 

size_a, size_b = group.get(root_a, 0), group.get(root_b, 0)
others = [size for root, size in group.items() if root != root_a and root != root_b]
others.sort(reverse = True)
print(size_a + sum(others[:k]))
