class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n = int(input())
q = int(input())
node = {i: Node(i) for i in range(1, n + 1)}

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if node[query[1]].prev:
            node[query[1]].prev.next = node[query[1]].next
        if node[query[1]].next:
            node[query[1]].next.prev = node[query[1]].prev
        node[query[1]].prev = None
        node[query[1]].next = None
    elif query[0] == 2:
        i_node, j_node = node[query[1]], node[query[2]]
        if i_node.prev:
            i_node.prev.next = j_node
            j_node.prev = i_node.prev
        j_node.next = i_node
        i_node.prev = j_node
    elif query[0] == 3:
        i_node, j_node = node[query[1]], node[query[2]]
        if i_node.next:
            i_node.next.prev = j_node
            j_node.next = i_node.next
        j_node.prev = i_node
        i_node.next = j_node
    elif query[0] == 4:
        prev_node, next_node = 0, 0
        if node[query[1]].prev:
            prev_node = node[query[1]].prev.data
        if node[query[1]].next:
            next_node = node[query[1]].next.data
        print(prev_node, next_node)

for i in range(1, n + 1):
    if node[i].next:
        print(node[i].next.data, end = ' ')
    else:
        print(0, end = ' ')