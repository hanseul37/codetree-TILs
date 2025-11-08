n, k = map(int, input().split())
q = int(input())
prev = [0] * (n + 1)
next = [0] * (n + 1)
head = [0] * k
tail = [0] * k

for i in range(2, n + 1):
    prev[i] = i - 1
    next[i - 1] = i
head[0], tail[0] = 1, n

for _ in range(q):
    op, i, j = map(int, input().split())
    i -= 1
    j -= 1
    if op == 1:
        if not head[i]:
            continue
        book = head[i]
        head[i] = next[book]
        if head[i]:
            prev[head[i]] = 0
        else:
            tail[i] = 0
        if tail[j]:
            next[tail[j]] = book
        else:
            head[j] = book
        prev[book] = tail[j]
        tail[j] = book
        next[book] = 0

    elif op == 2:
        if not tail[i]:
            continue
        book = tail[i]
        tail[i] = prev[book]
        if tail[i]:
            next[tail[i]] = 0
        else:
            head[i] = 0
        if head[j]:
            prev[head[j]] = book
        else:
            tail[j] = book
        next[book] = head[j]
        head[j] = book
        prev[book] = 0

    elif op == 3:
        if i == j or not head[i]:
            continue
        next[tail[i]] = head[j]
        if head[j]:
            prev[head[j]] = tail[i]
        else:
            tail[j] = tail[i]
        head[j] = head[i]
        head[i] = tail[i] = 0

    elif op == 4:
        if i == j or not head[i]:
            continue
        prev[head[i]] = tail[j]
        if tail[j]:
            next[tail[j]] = head[i]
        else:
            head[j] = head[i]
        tail[j] = tail[i]
        head[i] = tail[i] = 0

for i in range(k):
    point = head[i]
    books = []
    while point:
        books.append(point)
        point = next[point]
    print(len(books), *books)
