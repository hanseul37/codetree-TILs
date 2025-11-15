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
        circle_a, circle_b = circle_id[a], circle_id[b]
        if circle_a == circle_b:
            continue
        a_next, b_prev = circle[circle_a][a].next, circle[circle_b][b].prev
        a_next.prev = b_prev
        b_prev.next = a_next
        circle[circle_a][a].next = circle[circle_b][b]
        circle[circle_b][b].prev = circle[circle_a][a]
        for student in list(circle[circle_b].keys()):
            circle_id[student] = circle_a
            circle[circle_a][student] = circle[circle_b][student]
        circle[circle_b] = {}
    
    elif op[0] == 2:
        a, b = op[1], op[2]
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
        
