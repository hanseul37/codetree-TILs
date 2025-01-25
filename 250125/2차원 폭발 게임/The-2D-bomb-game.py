n, m, k = map(int, input().split())
bombs = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for _ in range(k):
    for i in range(n):
        target = bombs[0][i]
        new_line, temp = [], []
        flag = 1
        while flag:
            flag = 0
            for j in range(n):
                if bombs[j][i] == target:
                    temp.append(bombs[j][i])
                else:
                    if len(temp) < m:
                        new_line += temp
                    temp = [bombs[j][i]]
                    target = bombs[j][i]
            if len(temp) < m and target is not 0:
                flag = 1
                new_line += temp
            for j in range(n - len(new_line)):
                bombs[j][i] = 0
            for j in range(n - len(new_line), n):
                bombs[j][i] = new_line[j - n + len(new_line)]




    new_bombs = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_bombs[j][i] = bombs[n - i - 1][j]
    
    for i in range(n):
        line = []
        for j in range(n):
            if new_bombs[j][i] != 0:
                line.append(new_bombs[j][i])
        for j in range(n - len(line)):
            new_bombs[j][i] = 0
        for j in range(n - len(line), n):
            new_bombs[j][i] = line[j - n + len(line)]
    bombs = new_bombs

for i in range(n):
    target = bombs[0][i]
    new_line, temp = [], []
    flag = 1
    while flag:
        flag = 0
        for j in range(n):
            if bombs[j][i] == target:
                temp.append(bombs[j][i])
            else:
                if len(temp) < m:
                    new_line += temp
                temp = [bombs[j][i]]
                target = bombs[j][i]
        if len(temp) < m and target is not 0:
            flag = 1
            new_line += temp
        for elem in new_line:
            if elem != 0:
                cnt += 1

print(cnt)

        