n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r -= 1
c -= 1
if dir == 0:
    temp = arr[r][c]
    for i in range(m1):
        r -= 1
        c += 1
        temp, arr[r][c] = arr[r][c], temp
    for i in range(m2):
        r -= 1
        c -= 1
        temp, arr[r][c] = arr[r][c], temp 
    for i in range(m3):
        r += 1
        c -= 1
        temp, arr[r][c] = arr[r][c], temp
    for i in range(m4):
        r += 1
        c += 1
        temp, arr[r][c] = arr[r][c], temp
        
else:
    temp = arr[r][c]
    for i in range(m4):
        r -= 1
        c -= 1
        temp, arr[r][c] = arr[r][c], temp
    for i in range(m3):
        r -= 1
        c += 1
        temp, arr[r][c] = arr[r][c], temp 
    for i in range(m2):
        r += 1
        c += 1
        temp, arr[r][c] = arr[r][c], temp
    for i in range(m1):
        r += 1
        c -= 1
        temp, arr[r][c] = arr[r][c], temp 

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
