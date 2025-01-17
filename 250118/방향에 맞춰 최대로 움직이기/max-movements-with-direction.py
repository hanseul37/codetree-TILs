n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
max_cnt = 0

def moving(r, c, cnt):
    global max_cnt
    if not (0 <= r < n and 0 <= c < n):
        return
    flag = False
    for i in range(1, n):
        if not (0 <= r + dys[move_dir[r][c] - 1] * i < n and 0 <= c + dxs[move_dir[r][c] - 1] * i < n):
            break
        elif arr[r + dys[move_dir[r][c] - 1] * i][c + dxs[move_dir[r][c] - 1] * i] > arr[r][c]:
            moving(r + dys[move_dir[r][c] - 1] * i, c + dxs[move_dir[r][c] - 1] * i, cnt + 1)  
            flag = True
    if not flag:
        max_cnt = max(max_cnt, cnt)

moving(r - 1, c - 1, 0)
print(max_cnt)
        