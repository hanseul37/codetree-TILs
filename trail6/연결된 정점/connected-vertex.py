import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [int(i) for i in range(n + 1)]
size = [1] * (n + 1)

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        arr[root_x] = root_y
        size[root_y] += size[root_x]

for _ in range(m):
    command = list(input().split())
    if command[0] == 'x':
        union(int(command[1]), int(command[2]))
    else:
        print(size[find(int(command[1]))])