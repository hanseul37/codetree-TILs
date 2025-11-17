class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m, q = map(int, input().split())
circle, circle_id = [], {}
circle_min_student = []  # 각 그룹의 최솟값을 저장

# 초기화
for i in range(m):
    circle_len, *points = map(int, input().split())
    students = {st:Node(st) for st in points}
    for j in range(circle_len):
        students[points[j]].prev = students[points[j - 1]]
        students[points[j - 1]].next = students[points[j]]
    circle.append(students)
    circle_min_student.append(min(points))  # 그룹의 최솟값 저장
    for st in points:
        circle_id[st] = i

for _ in range(q):
    op = list(map(int, input().split()))
    
    # 1. 그룹 병합
    if op[0] == 1:
        a, b = op[1], op[2]
        circle_a_idx, circle_b_idx = circle_id[a], circle_id[b]
        if circle_a_idx == circle_b_idx:
            continue

        a_node = circle[circle_a_idx][a]
        b_node = circle[circle_b_idx][b]
        a_next, b_prev = a_node.next, b_node.prev

        a_next.prev = b_prev
        b_prev.next = a_next
        a_node.next = b_node
        b_node.prev = a_node

        if len(circle[circle_a_idx]) < len(circle[circle_b_idx]):
            # a 그룹이 더 작으면 b 그룹으로 합병
            new_min = min(circle_min_student[circle_a_idx], circle_min_student[circle_b_idx])
            circle_min_student[circle_b_idx] = new_min
            
            for student, node in circle[circle_a_idx].items():
                circle_id[student] = circle_b_idx
                circle[circle_b_idx][student] = node
            circle[circle_a_idx] = {}
            circle_min_student[circle_a_idx] = None
        else:
            # b 그룹이 더 작거나 같으면 a 그룹으로 합병
            new_min = min(circle_min_student[circle_a_idx], circle_min_student[circle_b_idx])
            circle_min_student[circle_a_idx] = new_min

            for student, node in circle[circle_b_idx].items():
                circle_id[student] = circle_a_idx
                circle[circle_a_idx][student] = node
            circle[circle_b_idx] = {}
            circle_min_student[circle_b_idx] = None

    # 2. 그룹 분리
    elif op[0] == 2:
        a, b = op[1], op[2]
        if circle_id[a] != circle_id[b]:
            continue
        circle_idx = circle_id[a]
        
        a_prev, b_prev = circle[circle_idx][a].prev, circle[circle_idx][b].prev
        a_prev.next = circle[circle_idx][b]
        b_prev.next = circle[circle_idx][a]
        circle[circle_idx][a].prev = b_prev
        circle[circle_idx][b].prev = a_prev

        # b를 포함하는 새로운 그룹 생성
        new_circle = {}
        new_circle_min = float('inf')
        cur = circle[circle_idx][b]
        while True:
            new_circle[cur.data] = cur
            new_circle_min = min(new_circle_min, cur.data)
            circle_id[cur.data] = len(circle)
            cur = cur.next
            if cur == circle[circle_idx][b]:
                break
        
        circle.append(new_circle)
        circle_min_student.append(new_circle_min)

        # 기존 그룹에서 new_circle의 학생들 삭제
        for student in new_circle:
            del circle[circle_idx][student]
        
        # 기존 그룹에 학생이 남아있으면 최솟값 재계산
        if circle[circle_idx]:
             circle_min_student[circle_idx] = min(circle[circle_idx].keys())
        else:
             circle_min_student[circle_idx] = None

    # 3. 그룹 출력
    elif op[0] == 3:
        a = op[1]
        circle_idx = circle_id[a]
        if not circle[circle_idx]: continue

        # 저장된 최솟값을 O(1)에 가져옴
        min_student = circle_min_student[circle_idx]
        cur = circle[circle_idx][min_student]
        
        output = []
        while True:
            output.append(str(cur.data))
            cur = cur.prev
            if cur == circle[circle_idx][min_student]:
                break
        print(' '.join(output))