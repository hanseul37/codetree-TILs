class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m, q = map(int, input().split())

circle = []
circle_id = {}

# 원을 대표 노드만 저장하는 방식으로 생성
for i in range(m):
    circle_len, *points = map(int, input().split())
    nodes = {p: Node(p) for p in points}

    # 원형 연결
    for j in range(circle_len):
        a = points[j]
        b = points[(j + 1) % circle_len]
        nodes[a].next = nodes[b]
        nodes[b].prev = nodes[a]

    # 대표(head) 집어넣기
    head = nodes[points[0]]
    circle.append(head)

    # circle_id 등록
    for st in points:
        circle_id[st] = i


# node에 접근하는 방법: circle_id → head → 순회
def find_node(head, target):
    cur = head
    while True:
        if cur.data == target:
            return cur
        cur = cur.next


for _ in range(q):
    op = list(map(int, input().split()))

    # ------------------------------------------------
    # 1번: 두 원을 연결 (합치기)
    # ------------------------------------------------
    if op[0] == 1:
        a, b = op[1], op[2]
        ca, cb = circle_id[a], circle_id[b]

        if ca == cb:
            continue

        head_a = circle[ca]
        head_b = circle[cb]

        node_a = find_node(head_a, a)
        node_b = find_node(head_b, b)

        # a next / b prev 조작
        a_next = node_a.next
        b_prev = node_b.prev

        a_next.prev = b_prev
        b_prev.next = a_next

        node_a.next = node_b
        node_b.prev = node_a

        # b 원의 모든 학생의 circle_id 를 ca로 변경
        cur = head_b
        while True:
            circle_id[cur.data] = ca
            cur = cur.next
            if cur == head_b:
                break

        # cb 원은 사용하지 않음 (head를 None 처리)
        circle[cb] = None


    # ------------------------------------------------
    # 2번: 한 원을 두 개로 분리
    # ------------------------------------------------
    elif op[0] == 2:
        a, b = op[1], op[2]
        if circle_id[a] != circle_id[b]:
            continue

        cidx = circle_id[a]
        head = circle[cidx]

        node_a = find_node(head, a)
        node_b = find_node(head, b)

        # cut
        a_prev = node_a.prev
        b_prev = node_b.prev

        a_prev.next = node_b
        node_b.prev = a_prev

        b_prev.next = node_a
        node_a.prev = b_prev

        # b가 새로운 헤드
        new_head = node_b
        circle.append(new_head)
        new_idx = len(circle) - 1

        # new circle의 circle_id 업데이트
        cur = new_head
        while True:
            circle_id[cur.data] = new_idx
            cur = cur.next
            if cur == new_head:
                break


    # ------------------------------------------------
    # 3번: 출력
    # ------------------------------------------------
    elif op[0] == 3:
        a = op[1]
        cidx = circle_id[a]
        head = circle[cidx]

        # 최소값 찾기
        cur = head
        mn = head.data
        while True:
            mn = min(mn, cur.data)
            cur = cur.next
            if cur == head:
                break

        # 최소값에서 prev방향 출력
        start = find_node(head, mn)
        cur = start
        while True:
            print(cur.data, end=' ')
            cur = cur.prev
            if cur == start:
                break
        print()
