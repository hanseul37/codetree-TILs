class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

q = int(input())
line = {1: Node(1)}
idx = 2

def connect(start, end, new_start, new_end):
    if start:
        new_start.prev = start
        start.next = new_start
    if end:
        new_end.next = end
        end.prev = new_end

for _ in range(q):
    op = list(input().split())
    if op[0] == '3':
        front, back = line[int(op[1])].prev, line[int(op[1])].next
        if not front or not back:
            print(-1)
        else:
            print(front.data, back.data)
    else:
        a, b = int(op[1]), int(op[2])
        line[idx] = Node(idx)
        for i in range(idx + 1, idx + b):
            line[i] = Node(i)
            line[i - 1].next = line[i]
            line[i].prev = line[i - 1]
        if op[0] == '1':
            connect(line[a], line[a].next, line[idx], line[idx + b - 1])
        elif op[0] == '2':
            connect(line[a].prev, line[a], line[idx], line[idx + b - 1])
        idx += b
