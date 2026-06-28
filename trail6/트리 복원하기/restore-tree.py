n = int(input())
edges = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(i + 1, n):
        edges.append([i, j, line[j]])

edges.sort(key=lambda x:x[2])
arr, ans, edge_cnt = [i for i in range(n)], [], 0

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]
    
def union(x, y):
    arr[find(x)] = find(y)

for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        ans.append([v1, v2, weight])
        edge_cnt += 1
    if edge_cnt == n - 1:
        break
        
ans.sort()
for v1, v2, weight in ans:
    print(v1 + 1, v2 + 1, weight)