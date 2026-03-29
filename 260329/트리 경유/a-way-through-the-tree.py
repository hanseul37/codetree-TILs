n, q = map(int, input().split())
visited = [False] * (n + 1)
for _ in range(q):
    dest = int(input())
    cur, ans = dest, 0
    while cur > 0:
        if visited[cur]:
            ans = cur
        cur //= 2
    if ans == 0:
        visited[dest] = True
        print(0)
    else:
        print(ans)
