n = int(input())
arr = [list(input()) for _ in range(n)]
r1, c1, r2, c2 = -1, -1, -1, -1
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
min_cnt = n * n
visited = {}

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S':
            r1 = i
            c1 = j
            arr[i][j] = '.'
        if arr[i][j] == 'E':
            r2 = i
            c2 = j
            arr[i][j] = '.'

def check(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def find_coin(r, c, cnt, coin, prev_coin):
    global min_cnt

    if r == r2 and c == c2 and coin >= 3:
        min_cnt = min(min_cnt, cnt)
        return

    if (r, c, coin, prev_coin) in visited and visited[(r, c, coin, prev_coin)] <= cnt:
        return
    visited[(r, c, coin, prev_coin)] = cnt

    for i in range(4):
        if check(r + dys[i], c + dxs[i]):
            new_coin = coin
            new_prev_coin = prev_coin
            if arr[r + dys[i]][c + dxs[i]] != '.':
                if prev_coin == -1 or int(arr[r + dys[i]][c + dxs[i]]) > prev_coin:
                    new_coin += 1
                else:
                    new_coin = 1
                new_prev_coin = int(arr[r + dys[i]][c + dxs[i]])
            find_coin(r + dys[i], c + dxs[i], cnt + 1, new_coin, new_prev_coin)
find_coin(r1, c1, 0, 0, -1)
if min_cnt != n * n:
    print(min_cnt)
else:
    print(-1)