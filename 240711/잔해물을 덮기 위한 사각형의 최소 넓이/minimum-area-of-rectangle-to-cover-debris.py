Ax1, Ay1, Ax2, Ay2 = list(map(int, input().split()))
Bx1, By1, Bx2, By2 = list(map(int, input().split()))
arr = [
    [0 for i in range(2000)]
    for _ in range(2000)
]
for i in range(Ax1, Ax2):
    for j in range(Ay1, Ay2):
        arr[i + 1000][j + 1000] = 1

for i in range(Bx1, Bx2):
    for j in range(By1, By2):
        arr[i + 1000][j + 1000] = 0
    
xmin, ymin = 2000, 2000
xmax, ymax = -1, -1
for i in range(2000):
    for j in range(2000):
        if arr[i][j] == 1:
            if j < xmin:
                xmin = j
            if j > xmax:
                xmax = j
            if i < ymin:
                ymin = i
            if i > ymax:
                ymax = i

print((xmax - xmin + 1) * (ymax - ymin + 1))