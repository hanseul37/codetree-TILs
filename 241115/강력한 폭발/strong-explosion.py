n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
bomb_num = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bomb_num += 1

def check(x, y):
    return 0 <= x < n and 0 <= y < n

bomb_arr = []
max_cnt = 0
def bomb(num):
    global max_cnt
    if num > bomb_num:
        location = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 1:
                    location[i][j] = 1
                    if bomb_arr[cnt] == 1:
                        for k in range(1, 3):
                            if check(j, i - k):
                                location[i - k][j] = 1
                            if check(j, i + k):
                                location[i + k][j] = 1
                    elif bomb_arr[cnt] == 2:
                        if check(j, i - 1):
                            location[i - 1][j] = 1
                        if check(j, i + 1):
                            location[i + 1][j] = 1
                        if check(j - 1, i):
                            location[i][j - 1] = 1
                        if check(j + 1, i):
                            location[i][j + 1] = 1
                    elif bomb_arr[cnt] == 3:
                        if check(j - 1, i - 1):
                            location[i - 1][j - 1] = 1
                        if check(j - 1, i + 1):
                            location[i + 1][j - 1] = 1
                        if check(j + 1, i - 1):
                            location[i - 1][j + 1] = 1
                        if check(j + 1, i + 1):
                            location[i + 1][j + 1] = 1
                    cnt += 1
        cnt = 0
        for i in range(n):
            for j in range(n):
                if location[i][j] == 1:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)                                     
        return 
        
    for i in range(1, 4):
        bomb_arr.append(i)
        bomb(num + 1)
        bomb_arr.pop()

bomb(1)
print(max_cnt)