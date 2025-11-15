class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m, q = map(int, input().split())

circle_head = {}  # 원의 대표 노드
node_map = {}     # 학생 -> 노드

for i in range(m):
    vals = list(map(int, input().split()))
    length, points = vals[0], vals[1:]
    prev_node = None
    first_node = None
    for st in points:
        node = Node(st)
        node_map[st] = node
        if prev_node:
            prev_node.next = node
            node.prev = prev_node
        else:
            first_node = node
        prev_node = node
    # 원형 연결
    prev_node.next = first_node
    first_node.prev = prev_node
    # 대표 노드 기록
    for st in points:
        circle_head[st] = first_node

for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:  # merge a -> b
        a, b = op[1], op[2]
        head_a = circle_head[a]
        head_b = circle_head[b]
        if head_a == head_b:
            continue
        # 연결
        a_next = node_map[a].next
        b_prev = node_map[b].prev
        a_next.prev = b_prev
        b_prev.next = a_next
        node_map[a].next = node_map[b]
        node_map[b].prev = node_map[a]

        # circle_head 갱신
        cur = node_map[b]
        while True:
            circle_head[cur.data] = head_a
            cur = cur.next
            if cur == node_map[b]:
                break

    elif op[0] == 2:  # split a <-> b
        a, b = op[1], op[2]
        if circle_head[a] != circle_head[b]:
            continue
        a_prev = node_map[a].prev
        b_prev = node_map[b].prev
        a_prev.next = node_map[b]
        b_prev.next = node_map[a]
        node_map[a].prev = b_prev
        node_map[b].prev = a_prev

        # 새 원 대표 노드 갱신
        cur = node_map[b]
        while True:
            circle_head[cur.data] = node_map[b]
            cur = cur.next
            if cur == node_map[b]:
                break

    elif op[0] == 3:  # print
        a = op[1]
        head = circle_head[a]
        cur = head
        while True:
            print(cur.data, end=' ')
            cur = cur.prev
            if cur == head:
                break
        print()
