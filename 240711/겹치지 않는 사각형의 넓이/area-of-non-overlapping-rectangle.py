Ax1, Ay1, Ax2, Ay2 = list(map(int, input().split()))
Bx1, By1, Bx2, By2 = list(map(int, input().split()))
Mx1, My1, Mx2, My2 = list(map(int, input().split()))
arr = [
    [0 for i in range(2000)]
    for _ in range(2000)
]

for i in range(Ax1, Ax2):
    for j in range(Ay1, Ay2):
        arr[i][j] = 1
    
for i in range(Bx1, Bx2):
    for j in range(By1, By2):
        arr[i][j] = 1

for i in range(Mx1, Mx2):
    for j in range(My1, My2):
        arr[i][j] = 2

cnt = 0
for i in range(2000):
    for j in range(2000):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)