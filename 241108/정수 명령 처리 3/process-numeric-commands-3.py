from collections import deque

n = int(input())
dq = deque()
for i in range(n):
    command = list(input().split())
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        print(dq.popleft())
    elif command[0] == 'pop_back':
        print(dq.pop())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        print(dq[0])
    elif command[0] == 'back':
        print(dq[-1])