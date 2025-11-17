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

def change_head(original_head, new_head):
    for i in range(m):
        if head[i] == original_head:
            head[i] = new_head

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
        if not b.prev:
            change_head(b.data, a.data)
        if not a.prev:
            new_head_data = a.next.data if a.next else -1
            change_head(a.data, new_head_data)
        disconnect(a, a)
        connect(b.prev, b, a, a)
    elif op[0] == '2':
        a = arr[op[1]]
        if not a.prev:
            new_head_data = a.next.data if a.next else -1
            change_head(a.data, new_head_data)
        disconnect(a, a)
        del arr[a.data]
    elif op[0] == '3':
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
    if point != -1:
        while True:
            print(arr[point].data, end = ' ')
            if not arr[point].next:
                break
            point = arr[point].next.data
        print()
    else:
        print(-1)
