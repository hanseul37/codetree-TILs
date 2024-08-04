lines = []
for _ in range(3):
    line = list(map(int, input()))
    lines.append(line)

teams = []
def check(cnt):
    return cnt not in teams

for i in range(3):
    point = lines[i][0]
    cnt = []
    cnt.append(point)
    for j in range(3):
        if lines[i][j] != point:
            if lines[i][j] not in cnt:
                cnt.append(lines[i][j])
            point = lines[i][j]
    if len(cnt) == 2 and check(cnt):
        teams.append(cnt)
    
for i in range(3):
    point = lines[0][i]
    cnt = []
    cnt.append(point)
    for j in range(3):
        if lines[j][i] != point:
            if lines[j][i] not in cnt:
                cnt.append(lines[j][i])
            point = lines[j][i]
    if len(cnt) == 2 and check(cnt):
        teams.append(cnt)

point = lines[0][0]
cnt = []
cnt.append(point)
for i in range(3):
    if lines[i][i] != point:
        if lines[i][i] not in cnt:
            cnt.append(lines[i][i])
        point = lines[i][i]
if len(cnt) == 2 and check(cnt):
    teams.append(cnt)

point = lines[0][2]
cnt = []
cnt.append(point)
for i in range(3):
    if lines[i][2 - i] != point:
        if lines[i][2 - i] not in cnt:
            cnt.append(lines[i][2 - i])
        point = lines[i][2 - i]
if len(cnt) == 2 and check(cnt):
    teams.append(cnt)

print(len(teams))