class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, m = map(int, input().split())
knight = list(map(int, input().split()))
arr = {kn: Node(kn) for kn in knight}
for i in range(n):
    arr[knight[i]].prev = arr[knight[i - 1]]
    arr[knight[i - 1]].next = arr[knight[i]]

for _ in range(m):
    call = int(input())
    print(arr[call].next.data, arr[call].prev.data)
    arr[call].prev.next = arr[call].next
    arr[call].next.prev = arr[call].prev
    del arr[call]

