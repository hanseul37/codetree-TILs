import sys
input = sys.stdin.readline  

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 2. 전체 가중치 합을 미리 구함 (원본 리스트 컴프리헨션 유지)
total_weight = sum(edge[2] for edge in edges)

edges.sort(key=lambda x:x[2])
cnt, edge_cnt, arr = 0, 0, [i for i in range(n + 1)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)  # 3. [수정] arr[y] 대신 find(y)로 루트끼리 연결

for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
    if edge_cnt == n - 1:
        break

# 4. [수정] 원본 출력 형태 유지하되, 전체 가중치에서 빼서 출력
if n == 1:
    print(0)
elif edge_cnt == n - 1:
    print(total_weight - cnt)
else:
    print(0)
