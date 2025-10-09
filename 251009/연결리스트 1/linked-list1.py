class Node:
    def  __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
node = Node(input())
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == '1':
        new_node = Node(cmd[1])
        new_node.prev = node.prev
        new_node.next = node
        if new_node.prev:
            new_node.prev.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
    elif cmd[0] == '2':
        new_node = Node(cmd[1])
        new_node.prev = node
        new_node.next = node.next
        if new_node.prev:
            new_node.prev.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
    elif cmd[0] == '3' and node.prev:
        node = node.prev
    elif cmd[0] == '4' and node.next:
        node = node.next

    if node.prev:
        print(node.prev.data, end= ' ')
    else:
        print('(Null)', end= ' ')
    if node:
        print(node.data, end= ' ')
    else:
        print('(Null)', end= ' ')
    if node.next:
        print(node.next.data)
    else:
        print('(Null)')
