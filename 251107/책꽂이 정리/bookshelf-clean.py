import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
q = int(input())

# 각 노드의 prev, next, 현재 큐 번호
prev = [0] * (n + 1)
nxt = [0] * (n + 1)
belong = [0] * (n + 1)

# 각 큐의 head, tail
head = [0] * k
tail = [0] * k

# 초기 상태: 모두 1번 큐에
for i in range(1, n + 1):
    belong[i] = 0  # 0번째 큐
    if i > 1:
        prev[i] = i - 1
        nxt[i - 1] = i
head[0] = 1
tail[0] = n

for _ in range(q):
    op, i, j = map(int, input().split())
    i -= 1
    j -= 1
    if op == 1:  # i의 앞 -> j의 뒤
        if head[i] == 0:
            continue
        x = head[i]
        head[i] = nxt[x]
        if head[i]:
            prev[head[i]] = 0
        else:
            tail[i] = 0

        prev[x] = tail[j]
        if tail[j]:
            nxt[tail[j]] = x
        else:
            head[j] = x
        tail[j] = x
        nxt[x] = 0
        belong[x] = j

    elif op == 2:  # i의 뒤 -> j의 앞
        if tail[i] == 0:
            continue
        x = tail[i]
        tail[i] = prev[x]
        if tail[i]:
            nxt[tail[i]] = 0
        else:
            head[i] = 0

        nxt[x] = head[j]
        if head[j]:
            prev[head[j]] = x
        else:
            tail[j] = x
        head[j] = x
        prev[x] = 0
        belong[x] = j

    elif op == 3:  # i -> j (앞에서 뒤로 연결)
        if i == j or head[i] == 0:
            continue
        if head[j] == 0:
            head[j], tail[j] = head[i], tail[i]
        else:
            prev[head[j]] = tail[i]
            nxt[tail[i]] = head[j]
            head[j] = head[i]
        cur = head[i]
        while cur:
            belong[cur] = j
            cur = nxt[cur]
        head[i] = tail[i] = 0

    elif op == 4:  # i -> j (뒤에서 뒤로 연결)
        if i == j or head[i] == 0:
            continue
        if tail[j] == 0:
            head[j], tail[j] = head[i], tail[i]
        else:
            nxt[tail[j]] = head[i]
            prev[head[i]] = tail[j]
            tail[j] = tail[i]
        cur = head[i]
        while cur:
            belong[cur] = j
            cur = nxt[cur]
        head[i] = tail[i] = 0

# 출력
for i in range(k):
    res = []
    cur = head[i]
    while cur:
        res.append(cur)
        cur = nxt[cur]
    print(len(res), *res)
