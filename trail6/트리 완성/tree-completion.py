n, m = map(int, input().split())
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
        return True
    return False

remove_cnt = 0
for _ in range(m):
    v1, v2 = map(int, input().split())
    if not union(v1, v2):
        remove_cnt += 1

connect_cnt = 0
for i in range(1, n + 1):
    if arr[i] == i:
        connect_cnt += 1
print(remove_cnt + connect_cnt - 1)
