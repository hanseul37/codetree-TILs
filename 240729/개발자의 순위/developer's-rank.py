k, n = list(map(int, input().split()))
games = []
for _ in range(k):
    game = list(map(int, input().split()))
    games.append(game)

cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        flag = 0
        for l in range(k):
            if not games[l].index(i + 1) < games[l].index(j + 1):
                flag = 1
        if flag:
            continue
        cnt += 1

print(cnt)