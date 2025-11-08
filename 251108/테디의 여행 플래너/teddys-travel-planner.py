class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, q = map(int, input().split())
arr = list(input().split())
cities = {arr[i]: Node(arr[i]) for i in range(n)}
for i in range(n):
    cities[arr[i - 1]].next = cities[arr[i]]
    cities[arr[i]].prev = cities[arr[i - 1]]
pin = arr[0]

for _ in range(q):
    op = list(input().split())
    if op[0] == '1':
        if cities[pin].next:
            pin = cities[pin].next.data
    elif op[0] == '2':
        if cities[pin].prev:
            pin = cities[pin].prev.data
    elif op[0] == '3':
        target = cities[pin].next
        if target:
            target.next.prev = cities[pin]
            cities[pin].next = target.next
            del cities[target.data]
    elif op[0] == '4':
        cities[op[1]] = Node(op[1])
        cities[op[1]].next = cities[pin].next
        cities[op[1]].prev = cities[pin]
        cities[pin].next.prev = cities[op[1]]
        cities[pin].next = cities[op[1]]
    
    if cities[pin].prev == cities[pin].next:
        print(-1)
    else:
        print(cities[pin].prev.data, cities[pin].next.data)