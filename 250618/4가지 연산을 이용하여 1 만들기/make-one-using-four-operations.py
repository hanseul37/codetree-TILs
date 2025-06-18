from collections import deque
n = int(input())
q = deque([(n, 0)])

while q:
    num, cnt = q.popleft()
    if num == 1:
        print(cnt)
        break

    q.append([num + 1, cnt + 1])

    q.append([num - 1, cnt + 1])
    if num % 2 == 0:
        q.append([num // 2, cnt + 1])
    if num % 3 == 0:
        q.append([num // 3, cnt + 1])
    
