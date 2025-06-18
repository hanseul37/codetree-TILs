from collections import deque
n = int(input())
q = deque([(n, 0)])
visited = set()
visited.add(n)

while q:
    num, cnt = q.popleft()
    if num == 1:
        print(cnt)
        break
    if num + 1 not in visited: 
        q.append([num + 1, cnt + 1])
        visited.add(num + 1)
    if num - 1 not in visited: 
        q.append([num - 1, cnt + 1])
        visited.add(num - 1)
    if num % 2 == 0 and num // 2 not in visited:
        q.append([num // 2, cnt + 1])
        visited.add(num // 2)
    if num % 3 == 0 and num // 3 not in visited:
        q.append([num // 3, cnt + 1])
        visited.add(num // 3)
    
