class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n = int(input())
q = int(input())
arr = {i: Node(i) for i in range(1, n + 1)}
for i in range(1, n + 1):
    if i > 1:
        arr[i].prev = arr[i - 1]
    if i < n:
        arr[i].next = arr[i + 1]

for _ in range(q):
    a, b, c, d = map(int, input().split())
    A, B, C, D = arr[a], arr[b], arr[c], arr[d]
    A_prev, B_next, C_prev, D_next = A.prev, B.next, C.prev, D.next

    if B_next == C:
        if A_prev:
            A_prev.next = C
        C.prev = A.prev
        if D_next:
            D_next.prev = B
        B.next = D.next
        D.next = A
        A.prev = D

    elif D_next == A:
        if C_prev:
            C_prev.next = A
        A.prev = C.prev
        if B_next:
            B_next.prev = D
        D.next = B.next
        B.next = C
        C.prev = B

    else:
        if A_prev:
            A_prev.next = C
        C.prev = A_prev    
        if B_next:
            B_next.prev = D
        D.next = B_next
        if C_prev:
            C_prev.next = A
        A.prev = C_prev 
        if D_next:
            D_next.prev = B
        B.next = D_next

head = None
for idx in arr:
    if not arr[idx].prev:
        head = arr[idx]
        break
        
while head:
    print(head.data, end = ' ')
    head = head.next
