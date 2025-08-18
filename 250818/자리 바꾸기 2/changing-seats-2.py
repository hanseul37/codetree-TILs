n, k = map(int, input().split())
changes = [list(map(int, input().split())) for _ in range(k)]
human = [set() for _ in range(n)]
now = list(range(n)) 

for i in range(n):
    human[i].add(i)

for i in range(3 * k):
    a, b = changes[i % k][0] - 1, changes[i % k][1] - 1
    human[now[a]].add(b)
    human[now[b]].add(a)
    now[a], now[b] = now[b], now[a]

for i in range(n):
    print(len(human[i]))