from collections import deque
n = int(input())
q = deque([(n, 0)])
visited = [0] * 1000001

while q:
    num, cnt = q.popleft()
    if num == 1:
        print(cnt)
        break
    if not visited[num + 1]:
        q.append([num + 1, cnt + 1])
    if not visited[num - 1]:
        q.append([num - 1, cnt + 1])
    if num % 2 == 0 and not visited[num // 2]:
        q.append([num // 2, cnt + 1])
    if num % 3 == 0 and not visited[num // 3]:
        q.append([num // 3, cnt + 1])
    
