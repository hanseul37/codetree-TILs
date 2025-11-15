class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m, q = map(int, input().split())

circle = []          # 각 원의 dict
circle_id = {}       # 학생 → 원 인덱스
circle_min = []      # 각 원의 최소 학생 번호

for i in range(m):
    vals = list(map(int, input().split()))
    length, points = vals[0], vals[1:]
    nodes = {st: Node(st) for st in points}

    for j in range(length):
        nodes[points[j]].next = nodes[points[(j+1)%length]]
        nodes[points[j]].prev = nodes[points[(j-1)%length]]

    circle.append(nodes)
    circle_min.append(min(points))
    for st in points:
        circle_id[st] = i

for _ in range(q):
    op = list(map(int, input().split()))

    if op[0] == 1:  # merge a -> b
        a, b = op[1], op[2]
        ca, cb = circle_id[a], circle_id[b]
        if ca == cb:
            continue

        node_a = circle[ca][a]
        node_b = circle[cb][b]
        a_next = node_a.next
        b_prev = node_b.prev

        # 연결
        a_next.prev = b_prev
        b_prev.next = a_next
        node_a.next = node_b
        node_b.prev = node_a

        # 학생 ID만 갱신
        for st in circle[cb]:
            circle_id[st] = ca
            circle[ca][st] = circle[cb][st]

        circle[cb] = {}
        circle_min[ca] = min(circle_min[ca], circle_min[cb])

    elif op[0] == 2:  # split a <-> b
        a, b = op[1], op[2]
        ci = circle_id[a]
        if circle_id[b] != ci:
            continue

        node_a = circle[ci][a]
        node_b = circle[ci][b]
        a_prev = node_a.prev
        b_prev = node_b.prev

        # 연결
        a_prev.next = node_b
        b_prev.next = node_a
        node_a.prev = b_prev
        node_b.prev = a_prev

        # 새로운 원 생성
        new_circle = {}
        cur = node_b
        new_min = cur.data
        while True:
            new_circle[cur.data] = cur
            circle_id[cur.data] = len(circle)
            new_min = min(new_min, cur.data)
            cur = cur.next
            if cur == node_b:
                break
        circle.append(new_circle)
        circle_min.append(new_min)

        # 기존 원에서 삭제
        for st in new_circle:
            del circle[ci][st]
        circle_min[ci] = min(circle[ci].keys()) if circle[ci] else 10**9

    elif op[0] == 3:  # print
        a = op[1]
        ci = circle_id[a]
        start = circle_min[ci]
        cur = circle[ci][start]
        while True:
            print(cur.data, end=' ')
            cur = cur.prev
            if cur.data == start:
                break
        print()
