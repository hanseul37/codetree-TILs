lines = []
for _ in range(3):
    line = list(map(int, input()))
    lines.append(line)

teams = 0
for i in range(3):
    cnt = 0
    point = lines[i][0]
    for j in range(3):
        if lines[i][j] != point:
            cnt += 1
    if cnt == 1:
        teams += 1
    
for i in range(3):
    cnt = 0
    point = lines[0][i]
    for j in range(3):
        if lines[j][i] != point:
            cnt += 1
    if cnt == 1:
        teams += 1

cnt = 0
point = lines[0][0]
for i in range(3):
    if lines[i][i] != point:
        cnt += 1
if cnt == 1:
    teams += 1

cnt = 0
point = lines[0][2]
for i in range(3):
    if lines[i][2 - i] != point:
        cnt += 1
if cnt == 1:
    teams += 1

print(teams)