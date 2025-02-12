n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_value = 0
painted = []

def paint(cnt):
    global max_value
    if cnt == n:
        value = 0
        for i in range(n):
            value += arr[painted[i][0]][painted[i][1]]
        max_value = max(max_value, value)
    
    for i in range(n):
        flag = 0
        for j in range(len(painted)):
            if i == painted[j][1]:
                flag = 1
        if flag:
            continue
        painted.append((cnt, i))
        paint(cnt + 1)
        painted.pop()

paint(0)
print(max_value)