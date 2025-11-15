import sys

# 1. 빠른 입출력 적용
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 

n, m, q = map(int, input().split())
circle = [] # 각 동아리의 멤버 딕셔너리를 담는 리스트
circle_id = {} # 학생 번호 -> circle 리스트의 인덱스

for i in range(m):
    line = list(map(int, input().split()))
    circle_len = line[0]
    points = line[1:]
    
    students = {st:Node(st) for st in points}
    for j in range(circle_len):
        curr = students[points[j]]
        prev = students[points[j - 1]]
        curr.prev = prev
        prev.next = curr
        
    circle.append(students)
    for st in points:
        circle_id[st] = i

for _ in range(q):
    op = list(map(int, input().split()))
    
    # === 1. 합치기 (Small-to-Large Merge) ===
    if op[0] == 1:
        a, b = op[1], op[2]
        idx_a, idx_b = circle_id[a], circle_id[b]
        
        if idx_a == idx_b:
            continue

        # [최적화] 항상 '더 작은 쪽'을 '더 큰 쪽'으로 옮기도록 설정
        # idx_b(source) -> idx_a(target) 로 이동할 것임
        if len(circle[idx_b]) > len(circle[idx_a]):
            idx_a, idx_b = idx_b, idx_a # 변수 스왑 (큰 쪽이 idx_a가 됨)

        # 노드 연결 (순서는 a, b 변수 기준이므로 위 스왑과 무관하게 진행)
        # a의 뒤에 b를 붙임
        a_node = circle[circle_id[a]][a] # 주의: 스왑된 idx가 아닌 원래 ID로 접근
        b_node = circle[circle_id[b]][b]
        
        a_next = a_node.next
        b_prev = b_node.prev
        
        a_next.prev = b_prev
        b_prev.next = a_next
        a_node.next = b_node
        b_node.prev = a_node
        
        # 데이터 이동 (idx_b에 있는걸 idx_a로)
        source_dict = circle[idx_b]
        target_dict = circle[idx_a]
        
        for st_val, node in source_dict.items():
            circle_id[st_val] = idx_a # ID 갱신
            target_dict[st_val] = node # 딕셔너리 추가
        
        # 옮겨진 쪽은 비움
        circle[idx_b] = {}
    
    # === 2. 나누기 (Small-to-Large Split) ===
    elif op[0] == 2:
        a, b = op[1], op[2]
        idx_a, idx_b = circle_id[a], circle_id[b]
        
        # 연결 끊기
        a_node = circle[idx_a][a]
        b_node = circle[idx_b][b]
        
        a_prev = a_node.prev
        b_prev = b_node.prev
        
        # a와 b 사이를 끊음 -> 두 개의 고리로 만듦
        # 1번 고리: ... -> a_prev -> b -> ...
        # 2번 고리: ... -> b_prev -> a -> ...
        # (원래 a->b 였으므로 끊으면, a는 뒤가 끊기고 b는 앞이 끊김)
        
        # a_prev와 b를 연결 (잘못된 로직 수정: 원래 코드의 의도는 a와 b 사이를 끊는 것)
        # 원래 코드: a_prev -> b (X) 
        # 올바른 분리: a와 b 사이를 끊으면 a->...->a_prev(순환) 이렇게 되는게 아니라
        # a의 이전노드는 그대로, a의 다음노드가 b였음.
        # 끊으면: a의 다음은 b가 아님. b의 이전은 a가 아님.
        # a의 이전(a_prev) <-> b 연결? (X)
        # 문제 정의상: a와 b가 인접해있음. a->b 연결을 끊고, 역순으로 연결?
        # 사용자 코드의 로직을 따름: a_prev <-> b, b_prev <-> a
        
        a_prev.next = b_node
        b_node.prev = a_prev
        
        b_prev.next = a_node
        a_node.prev = b_prev
        
        # [최적화] 어느 쪽이 더 작은 덩어리인지 양방향 탐색으로 확인
        # cur1은 b에서 정방향, cur2는 a에서 역방향으로 탐색
        cur1, cur2 = b_node, a_node
        move_target = None # 0이면 b쪽(cur1)이 작음, 1이면 a쪽(cur2)이 작음
        
        while True:
            # b쪽 덩어리가 한바퀴 돌았는지 확인
            if cur1.next == b_node:
                move_target = 0 # b쪽 덩어리를 옮기자
                break
            # a쪽 덩어리가 한바퀴 돌았는지 확인
            if cur2.prev == a_node:
                move_target = 1 # a쪽 덩어리를 옮기자
                break
            
            cur1 = cur1.next
            cur2 = cur2.prev
            
            # (안전장치) 만약 둘이 만나거나 하면 이미 한바퀴 돈 것
            if cur1 == cur2: 
                move_target = 0 # 아무거나
                break

        # 결정된 작은 덩어리를 새 동아리로 이동
        new_circle = {}
        new_idx = len(circle)
        
        if move_target == 0:
            # b쪽 덩어리 이동
            start_node = b_node
            limit_node = b_node
            direction = 'next'
        else:
            # a쪽 덩어리 이동
            start_node = a_node
            limit_node = a_node
            direction = 'prev'
            
        curr = start_node
        origin_idx = idx_a # a나 b나 같은 동아리였음
        
        while True:
            # 이동할 노드 처리
            val = curr.data
            new_circle[val] = curr
            del circle[origin_idx][val] # 기존 딕셔너리에서 삭제
            circle_id[val] = new_idx # ID 갱신
            
            if direction == 'next':
                curr = curr.next
            else:
                curr = curr.prev
                
            if curr == limit_node:
                break
                
        circle.append(new_circle)

    elif op[0] == 3:
        a = op[1]
        idx = circle_id[a]
        
        if not circle[idx]:
            print()
            continue
            
        min_val = min(circle[idx].keys())
        curr = circle[idx][min_val]
        start = curr
        
        while True:
            print(curr.data, end=' ')
            curr = curr.prev
            if curr == start:
                break
        print()