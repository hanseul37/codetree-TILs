import heapq

n = int(input())
q = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        heapq.heappush(q, -int(command[1]))
    elif command[0] == 'pop':
        print(-heapq.heappop(q))
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    else:
        print(-q[0])

