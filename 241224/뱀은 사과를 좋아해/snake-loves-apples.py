n, m, k = map(int, input().split())
apples = [list(map(int, input().split())) for _ in range(m)]
turns = [list(input().split()) for _ in range(k)]

arr = [[0] * n for _ in range(n)]
for i in range(m):
    arr[apples[0] - 1][apples[1] - 1] = 1

snake = [[0, 0]]

def check(y, x):
    ans = 0
    for i in range(len(snake)):
        if snake[i][0] == y and snake[i][1] == x:
            ans = 1
            break
    if not 0 <= x < n and 0 <= y < n:
        ans = 1
    return ans

def find_apple(y, x):
    for i in range(len(apples)):
        if y == apples[i][0] - 1 and x == apples[i][1] - 1:
            return 1
    return 0

cnt, flag = 0, 0
for i in range(k):
    if flag:
        break
    
    if turns[i][0] == 'U':
        for j in range(int(turns[i][1])):
            if check(snake[-1][0] - 1, snake[-1][1]):
                flag = 1
                break 
            if find_apple(snake[-1][0] - 1, snake[-1][1]):
                snake.pop(0)
            snake.append([snake[-1][0] - 1, snake[-1][1]])
            cnt += 1
    elif turns[i][0] == 'D':
        for j in range(int(turns[i][1])):
            if check(snake[-1][0] + 1, snake[-1][1]):
                flag = 1
                break 
            if find_apple(snake[-1][0] + 1, snake[-1][1]):
                snake.pop(0)
            snake.append([snake[-1][0] + 1, snake[-1][1]])
            cnt += 1
    elif turns[i][0] == 'R':
        for j in range(int(turns[i][1])):
            if check(snake[-1][0], snake[-1][1] + 1):
                flag = 1
                break 
            if find_apple(snake[-1][0], snake[-1][1] + 1):
                snake.pop(0)
            snake.append([snake[-1][0], snake[-1][1] + 1])
            cnt += 1
    elif turns[i][0] == 'L':
        for j in range(int(turns[i][1])):
            if check(snake[-1][0], snake[-1][1] - 1):
                flag = 1
                break 
            if find_apple(snake[-1][0], snake[-1][1] - 1):
                snake.pop(0)
            snake.append([snake[-1][0], snake[-1][1] - 1])
            cnt += 1
print(cnt)