class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def connect(start, end, new_start, new_end):
    if start:
        new_start.prev = start
        start.next = new_start
    if end:
        new_end.next = end
        end.prev = new_end

def disconnect(start, end):
    if start.prev:
        start.prev.next = end.next
    if end.next:
        end.next.prev = start.prev
    start.prev = None
    end.next = None

n, m, q = map(int, input().split())
names = list(input().split())
arr = {}
head = [-1] * m
for i in range(n):
    arr[names[i]] = Node(names[i])
    if i % (n // m) == 0:
        head[i // (n // m)] = names[i]
    else:
        arr[names[i]].prev = arr[names[i - 1]]
        arr[names[i - 1]].next = arr[names[i]]

for _ in range(q):
    op = list(input().split())
    if op[0] == '1':
        a, b = arr[op[1]], arr[op[2]]
        
        a_was_head = (a.prev is None)
        b_was_head = (b.prev is None)
        
        new_head_for_a_list = a.next.data if a.next else -1
        
        a_list_idx, b_list_idx = -1, -1
        for i in range(m):
            if head[i] == a.data:
                a_list_idx = i
            elif head[i] == b.data:
                b_list_idx = i

        b_prev_node = b.prev
        disconnect(a, a)
        connect(b_prev_node, b, a, a)

        if a_was_head and a_list_idx != -1:
            head[a_list_idx] = new_head_for_a_list
        if b_was_head and b_list_idx != -1:
            head[b_list_idx] = a.data

    elif op[0] == '2':
        a = arr[op[1]]
        a_was_head = (a.prev is None)
        new_head_for_a_list = a.next.data if a.next else -1
        
        a_list_idx = -1
        if a_was_head:
            for i in range(m):
                if head[i] == a.data:
                    a_list_idx = i
                    break
        
        disconnect(a, a)
        del arr[a.data]

        if a_was_head and a_list_idx != -1:
            head[a_list_idx] = new_head_for_a_list

    elif op[0] == '3':
        a, b, c = arr[op[1]], arr[op[2]], arr[op[3]]

        a_was_head = (a.prev is None)
        c_was_head = (c.prev is None)

        new_head_for_a_list = b.next.data if b.next else -1

        a_list_idx, c_list_idx = -1, -1
        for i in range(m):
            if head[i] == a.data:
                a_list_idx = i
            elif head[i] == c.data:
                c_list_idx = i
        
        c_prev_node = c.prev
        disconnect(a, b)
        connect(c_prev_node, c, a, b)

        if a_was_head and a_list_idx != -1:
            head[a_list_idx] = new_head_for_a_list
        if c_was_head and c_list_idx != -1:
            head[c_list_idx] = a.data

for i in range(m):
    point = head[i]
    if point != -1:
        while True:
            print(arr[point].data, end = ' ')
            if not arr[point].next:
                break
            point = arr[point].next.data
        print()
    else:
        print(-1)
