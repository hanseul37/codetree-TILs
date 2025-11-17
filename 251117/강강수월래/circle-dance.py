MAX_N = 100000

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def connect_circle(u, v):
    v_prev = v.prev
    u_next = u.next

    connect(u, v)
    connect(v_prev, u_next)

def split_circle(u, v):
    u_prev = u.prev
    v_prev = v.prev

    connect(u_prev, v)
    connect(v_prev, u)

def print_line(target):
    mn = target.data
    cur = target
    while True:
        cur = cur.next  
        if cur is not None:
            mn = min(mn, cur.data)
        if cur == target:
            break

    init = nodes[student_id[mn]]
    cur = nodes[student_id[mn]]
    while True:
        print(cur.data, end=' ')
        cur = cur.prev
        if cur.data == init.data:
            break
    print()

n, m, q = map(int, input().split())
nodes = [None] * (MAX_N + 2)
student_id = {}
node_cnt = 1
for i in range(m):
    line = list(map(int, input().split()))
    circle_size = line[0]
    start = tail = None
    for j in range(1, circle_size + 1):
        student_num = line[j]
        student_id[student_num] = node_cnt
        nodes[node_cnt] = Node(student_num)

        if j == 1:
            start = tail = nodes[node_cnt]
        else:
            connect(tail, nodes[node_cnt])
            tail = nodes[node_cnt]
            if j == circle_size:
                connect(tail, start)
        node_cnt += 1

for _ in range(q):
    line = list(map(int, input().split()))
    option = line[0]

    if option == 1:
        a, b = line[1], line[2]
        connect_circle(nodes[student_id[a]], nodes[student_id[b]])

    elif option == 2:
        a, b = line[1], line[2]
        split_circle(nodes[student_id[a]], nodes[student_id[b]])

    elif option == 3:
        a = line[1]
        print_line(nodes[student_id[a]])
