n, m = map(int, input().split())
arr = [[list(map(int, x.split())) for x in input().split()] for _ in range(n)]
move = list(map(int, input().split()))
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def check(r, c):
    return 0 <= r < n and 0 <= c < n

for i in range(m):
    flag = 0
    for j in range(n):
        for k in range(n):
            if move[i] in arr[j][k] and flag == 0:
                max_value = 0
                t_x, t_y = k, j
                found = False

                for dy, dx in directions:
                    ny, nx = j + dy, k + dx
                    if check(ny, nx) and arr[ny][nx]:
                        found = True
                        if max(arr[ny][nx]) > max_value:
                            t_x, t_y = nx, ny
                            max_value = max(arr[ny][nx])
                
                if not found:
                    continue

                temp = []
                for l in range(len(arr[j][k])):
                    temp.append(arr[j][k][l])
                    if arr[j][k][l] == move[i]:
                        arr[j][k] = arr[j][k][l + 1:]
                        break
                for l in range(len(arr[t_y][t_x])):
                    temp.append(arr[t_y][t_x][l])
                arr[t_y][t_x] = temp
                flag = 1
                
for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            print("None")
        else:
            for elem in arr[i][j]:
                print(elem, end=' ')
            print()
