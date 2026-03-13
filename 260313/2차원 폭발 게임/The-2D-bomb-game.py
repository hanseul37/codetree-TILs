n, m, k = map(int, input().split())
bombs = [list(map(int, input().split())) for _ in range(n)]

def explosion(bombs):
    new_bombs = [[0] * n for _ in range(n)]
    for i in range(n):
        not_explosion, point, cnt = [], bombs[0][i], 1
        for j in range(1, n):
            if bombs[j][i] == point:
                cnt += 1
            else:
                if cnt < m:
                    for _ in range(cnt):
                        if point != 0:
                            not_explosion.append(point)
                point = bombs[j][i]
                cnt = 1
        if cnt < m:
            for _ in range(cnt):
                if point != 0:
                    not_explosion.append(point)
        for j in range(len(not_explosion)):
            new_bombs[n - len(not_explosion) + j][i] = not_explosion[j]
    return new_bombs

def turn(bombs):
    new_bombs = [[0] * n for _ in range(n)]
    for i in range(n):
        not_explosion = []
        for j in range(n):
            if bombs[n - 1 - i][j]:
                not_explosion.append(bombs[n - 1 - i][j])
        for j in range(len(not_explosion)):
            new_bombs[n - len(not_explosion) + j][i] = not_explosion[j]
    return new_bombs
        
for _ in range(k):
    while True:
        new_bombs = explosion(bombs)
        if bombs == new_bombs:
            break
        bombs = new_bombs
    bombs = turn(bombs)
while True:
    new_bombs = explosion(bombs)
    if bombs == new_bombs:
        break
    bombs = new_bombs

cnt = 0
for i in range(n):
    for j in range(n):
        if bombs[i][j]:
            cnt += 1
print(cnt)