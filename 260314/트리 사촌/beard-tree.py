n, k = map(int, input().split())
sequence = list(map(int, input().split()))
tree = [[] for _ in range(n)]
parent = [-1] * n 
parent_idx = -1
for i in range(1, n):
    if sequence[i] != sequence[i - 1] + 1:
        parent_idx += 1        
    tree[parent_idx].append(i)
    parent[i] = parent_idx

target = sequence.index(k)
if parent[target] == -1 or parent[parent[target]] == -1:
    print(0)
else:
    cnt = 0
    for node in tree[parent[parent[target]]]:
        if node != parent[target]: 
            cnt += len(tree[node])           
    print(cnt)