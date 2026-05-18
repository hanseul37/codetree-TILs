n = int(input())
arr = [int(i) for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return arr[x]
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        if root_x < root_y:
            arr[root_y] = root_x
        else:
            arr[root_x] = root_y
    arr[find(x)] = find(y)

for _ in range(n - 2):
    v1, v2 = map(int, input().split())
    union(v1, v2)

first = find(1)
for i in range(2, n + 1):
    if find(i) != first:
        second = find(i)
        break

print(min(first, second), max(first, second))