class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m, q = map(int, input().split())
arr = dict()
head = [-1] * m
for i in range(m):
    line = list(map(int, input().split()))
    if line[0] != -1:
        arr[line[1]] = Node(line[1])
        head[i] = line[1]
        for j in range(2, len(line)):
            arr[line[j]] = Node(line[j])
            arr[line[j - 1]].next = arr[line[j]]
            arr[line[j]].prev = arr[line[j - 1]]

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

def change_head(original_head, new_head):
    for i in range(m):
        if head[i] == original_head:
            head[i] = new_head

for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        a, b = arr[op[1]], arr[op[2]]
        if not b.prev:
            change_head(b.data, a.data)
        if not a.prev:
            new_head_data = a.next.data if a.next else -1
            change_head(a.data, new_head_data)
        disconnect(a, a)
        connect(b.prev, b, a, a)
    elif op[0] == 2:
        a = arr[op[1]]
        if not a.prev:
            new_head_data = a.next.data if a.next else -1
            change_head(a.data, new_head_data)
        disconnect(a, a)
        del arr[a.data]
    elif op[0] == 3:
        a, b, c = arr[op[1]], arr[op[2]], arr[op[3]]
        if not c.prev:
            change_head(c.data, a.data)
        if not a.prev:
            new_head_data = b.next.data if b.next else -1
            change_head(a.data, new_head_data)
        disconnect(a, b)   
        connect(c.prev, c, a, b)        

for i in range(m):
    point = head[i]
    if point > -1:
        while True:
            print(arr[point].data, end = ' ')
            if not arr[point].next:
                break
            point = arr[point].next.data
        print()
    else:
        print(-1)
