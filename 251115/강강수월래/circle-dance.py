class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m, q = map(int, input().split())
circle, circle_id = [], {}
circle_mins = [] 

for i in range(m):
    circle_len, *points = map(int, input().split())
    students = {st:Node(st) for st in points}
    for j in range(circle_len):
        students[points[j]].prev = students[points[j - 1]]
        students[points[j - 1]].next = students[points[j]]
    circle.append(students)
    circle_mins.append(min(points))
    for st in points:
        circle_id[st] = i

for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        a, b = op[1], op[2]
        if a not in circle_id or b not in circle_id:
            continue
        circle_a_idx, circle_b_idx = circle_id[a], circle_id[b]
        if circle_a_idx == circle_b_idx:
            continue

        if len(circle[circle_a_idx]) < len(circle[circle_b_idx]):
            a, b = b, a
            circle_a_idx, circle_b_idx = circle_b_idx, circle_a_idx
        
        old_min_a = circle_mins[circle_a_idx]
        old_min_b = circle_mins[circle_b_idx]

        a_next = circle[circle_a_idx][a].next
        b_prev = circle[circle_b_idx][b].prev

        a_next.prev = b_prev
        b_prev.next = a_next

        circle[circle_a_idx][a].next = circle[circle_b_idx][b]
        circle[circle_b_idx][b].prev = circle[circle_a_idx][a]

        for student in circle[circle_b_idx]:
            circle_id[student] = circle_a_idx
        
        circle[circle_a_idx].update(circle[circle_b_idx])
        circle[circle_b_idx] = {}
        
        circle_mins[circle_a_idx] = min(old_min_a, old_min_b)
        circle_mins[circle_b_idx] = None

    elif op[0] == 2:
        a, b = op[1], op[2]
        if a not in circle_id or b not in circle_id or circle_id[a] != circle_id[b]:
            continue
        circle_idx = circle_id[a]
        
        old_min = circle_mins[circle_idx]

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
        
        for student in new_circle:
            del circle[circle_idx][student]
        
        circle.append(new_circle)
        
        circle_mins.append(min(new_circle.keys()))
        if old_min in new_circle:
            if circle[circle_idx]:
                circle_mins[circle_idx] = min(circle[circle_idx].keys())
            else:
                circle_mins[circle_idx] = None

    elif op[0] == 3:
        a = op[1]
        if a not in circle_id:
            continue
        circle_idx = circle_id[a]
        if not circle[circle_idx]:
            continue

        min_student = circle_mins[circle_idx]
        cur = circle[circle_idx][min_student]
        
        start_node = cur
        while True:
            print(cur.data, end=' ')
            cur = cur.prev
            if cur == start_node:
                break
        print()
