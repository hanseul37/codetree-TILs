class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 

n, m, q = map(int, input().split())
circle, circle_id = [], {}
for i in range(m):
    circle_len, *points = map(int, input().split())
    students = {st:Node(st) for st in points}
    for j in range(circle_len):
        students[points[j]].prev = students[points[j - 1]]
        students[points[j - 1]].next = students[points[j]]
    circle.append(students)
    for st in points:
        circle_id[st] = i

for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        a, b = op[1], op[2]
        circle_a_idx, circle_b_idx = circle_id[a], circle_id[b]
        if circle_a_idx == circle_b_idx:
            continue

        # 포인터 연결 로직은 a, b를 그대로 사용해야 합니다.
        a_node = circle[circle_a_idx][a]
        b_node = circle[circle_b_idx][b]
        a_next, b_prev = a_node.next, b_node.prev

        a_next.prev = b_prev
        b_prev.next = a_next
        a_node.next = b_node
        b_node.prev = a_node

        # 데이터 이동 시에만 크기 비교를 사용합니다.
        # 작은 그룹을 큰 그룹으로 합칩니다.
        if len(circle[circle_a_idx]) < len(circle[circle_b_idx]):
            # a의 그룹이 더 작으므로, a 그룹의 학생들을 b 그룹으로 옮깁니다.
            for student, node in circle[circle_a_idx].items():
                circle_id[student] = circle_b_idx
                circle[circle_b_idx][student] = node
            circle[circle_a_idx] = {}
        else:
            # b의 그룹이 더 작거나 같으므로, b 그룹의 학생들을 a 그룹으로 옮깁니다.
            for student, node in circle[circle_b_idx].items():
                circle_id[student] = circle_a_idx
                circle[circle_a_idx][student] = node
            circle[circle_b_idx] = {}
    
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

        new_circle = {}
        cur = circle[circle_idx][b]
        while True:
            new_circle[cur.data] = cur
            circle_id[cur.data] = len(circle)
            cur = cur.next
            if cur == circle[circle_idx][b]:
                break
        circle.append(new_circle)

        for student in new_circle:
            del circle[circle_idx][student]
    
    elif op[0] == 3:
        a = op[1]
        circle_idx = circle_id[a]
        min_student = min(circle[circle_idx].keys())
        cur = circle[circle_idx][min_student]
        while True:
            print(cur.data, end=' ')
            cur = cur.prev
            if cur == circle[circle_idx][min_student]:
                break
        
