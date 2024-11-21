n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = [list(input().split()) for _ in range(q)]

def change(location, direction, side):
    if direction == 'L':
        temp = arr[location][-1]
        for i in range(m - 1, 0, -1):
            arr[location][i] = arr[location][i - 1]
        arr[location][0] = temp
        direction = 'R'
    else:
        temp = arr[location][0]
        for i in range(m - 1):
            arr[location][i] = arr[location][i + 1]
        arr[location][-1] = temp
        direction = 'L'
    
    if location != 0 and (side == 'U' or side == 'UD'):
        for i in range(m):
            if arr[location][i] == arr[location - 1][i]:
                change(location - 1, direction, 'U')
                break
        
    if location != n - 1 and (side == 'D' or side == 'UD'):
        for i in range(m):
            if arr[location][i] == arr[location + 1][i]:
                change(location + 1, direction, 'D')
                break    
         
    return 


for i in range(q):
    if int(winds[i][0]) == 1:
        change(int(winds[i][0]) - 1, winds[i][1], 'D')
    elif int(winds[i][0]) == n:
        change(int(winds[i][0]) - 1, winds[i][1], 'U')
    else:
        change(int(winds[i][0]) - 1, winds[i][1], 'UD')

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()
