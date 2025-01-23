n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]
flag = True

while flag and len(bombs) > 0:
    new_bombs, temp = [], []
    target = bombs[0]
    flag = False
    for i in range(len(bombs)):
        if bombs[i] != target:
            target = bombs[i]
            if len(temp) < m:
                new_bombs += temp
            else:
                flag = True
            temp = [target] 
        else:
            temp.append(bombs[i])
    if len(temp) < m:
        new_bombs += temp
    bombs = new_bombs

print(len(bombs))
for bomb in bombs:
    print(bomb)
