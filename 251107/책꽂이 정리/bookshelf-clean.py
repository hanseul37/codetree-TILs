from collections import deque

n, k = map(int, input().split())
q = int(input())
arr = [deque() for _ in range(k)]
for i in range(1, n + 1):
    arr[0].append(i)

for _ in range(q):
    op, i, j = map(int, input().split())
    i -= 1
    j -= 1
    if op == 1:
        if arr[i]:
            arr[j].append(arr[i].popleft())
    elif op == 2:
        if arr[i]:
            arr[j].appendleft(arr[i].pop())
    elif op == 3:
        if i == j: 
            continue
        arr[j].extendleft(reversed(arr[i]))
        arr[i].clear()
    elif op == 4:
        if i == j: 
            continue
        arr[j].extend(arr[i])
        arr[i].clear()

for i in range(k):
    print(len(arr[i]), end = ' ')
    for elem in arr[i]:
        print(elem, end = ' ')
    print()
