import sys
input = sys.stdin.readline

# 1. 초기 세팅 및 트리 구성 (작성하신 부분)
n, m = map(int, input().split())
tree, weight = [[] for _ in range(n + 1)], [0] * (n + 1)

# parent 리스트: [-1, 1, 1, 2, ...] 형태로 입력됨
parent = list(map(int, input().split()))

# 인덱스 1(2번 노드)부터 N-1(N번 노드)까지 순회하며 트리 구성
for i in range(1, n):
    # 단, 부모에서 자식으로만 탐색할 것이므로 단방향(부모->자식)만 연결해도 충분합니다.
    tree[parent[i]].append(i + 1)
    # tree[i + 1].append(parent[i]) <- 이 줄은 지워도 무방합니다.

# 2. M개의 연산 처리 (자기 자신에게만 점수 누적)
for _ in range(m):
    node, w = map(int, input().split())
    weight[node] += w

# 3. 점수 내리물림 (위상 정렬의 성질 활용)
# 2번 노드(인덱스 1)부터 N번 노드(인덱스 n-1)까지 순서대로 부모의 점수를 더해줌
for i in range(1, n):
    current_node = i + 1
    parent_node = parent[i]
    
    weight[current_node] += weight[parent_node]

# 4. 결과 출력 (1번 노드부터 N번 노드까지)
print(*weight[1:])