from collections import deque
n, k = map(int, input().split())
q = deque()
for i in range(n):
    q.append(i + 1)
while len(q) != 0:
    for i in range(k):
        q.append(q.popleft())
    print(q.pop(), end=' ')