import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = int(input())

# 링크드 리스트용 배열
prev = [0] * (n + 1)
nxt = [0] * (n + 1)

# 각 큐의 head, tail
head = [0] * k
tail = [0] * k

# 초기화: 모든 원소는 1번 큐에 순서대로 연결
for i in range(1, n + 1):
    if i > 1:
        prev[i] = i - 1
        nxt[i - 1] = i
head[0], tail[0] = 1, n

# 나머지 큐는 비어 있음
for i in range(1, k):
    head[i] = tail[i] = 0

# 연산 처리
for _ in range(q):
    op, i, j = map(int, input().split())
    i -= 1
    j -= 1

    # 1. i의 맨 앞을 j의 뒤로
    if op == 1:
        if not head[i]:
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

    # 2. i의 맨 뒤를 j의 앞으로
    elif op == 2:
        if not tail[i]:
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

    # 3. i 전체를 j의 앞으로
    elif op == 3:
        if i == j or not head[i]:
            continue
        nxt[tail[i]] = head[j]
        if head[j]:
            prev[head[j]] = tail[i]
        else:
            tail[j] = tail[i]
        head[j] = head[i]
        head[i] = tail[i] = 0

    # 4. i 전체를 j의 뒤로
    elif op == 4:
        if i == j or not head[i]:
            continue
        prev[head[i]] = tail[j]
        if tail[j]:
            nxt[tail[j]] = head[i]
        else:
            head[j] = head[i]
        tail[j] = tail[i]
        head[i] = tail[i] = 0

# 출력
for i in range(k):
    cur = head[i]
    res = []
    while cur:
        res.append(cur)
        cur = nxt[cur]
    print(len(res), *res)
