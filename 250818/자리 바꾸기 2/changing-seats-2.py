n, k = map(int, input().split())
changes = [list(map(int, input().split())) for _ in range(k)]
human = [set() for _ in range(n)]
now = []

for i in range(n):
    human[i].add(i)
    now.append(i)

for i in range(3 * k):
    a, b = changes[i % k][0] - 1, changes[i % k][1] - 1
    now[a], now[b] = now[b], now[a]
    human[now[a]].add(b)
    human[now[b]].add(a)

for i in range(n):
    print(len(human[i]))