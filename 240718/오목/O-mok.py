board = []
for _ in range(19):
    room = input().split()
    board.append(room)

def in_range1(x, y):
    return y + 4 < 19

def in_range2(x, y):
    return x + 4 < 19

def in_range3(x, y):
    return x + 4 < 19 and y + 4 < 19

def in_range4(x, y):
    return x - 4 >= 0 and y + 4 < 19

winner = 0
x, y = -1, -1
for i in range(19):
    for j in range(19):
        if board[i][j] == '1':
            if in_range1(j, i) and board[i + 1][j] == '1' and board[i + 2][j] == '1' and board[i + 3][j] == '1' and board[i + 4][j] == '1':
                winner = 1
                y, x = i + 3, j + 1
            elif in_range2(j, i) and board[i][j + 1] == '1' and board[i][j + 2] == '1' and board[i][j + 3] == '1' and board[i][j + 4] == '1':
                winner = 1
                y, x = i + 1, j + 3
            elif in_range3(j, i) and board[i + 1][j + 1] == '1' and board[i + 2][j + 2] == '1' and board[i + 3][j + 3] == '1' and board[i + 4][j + 4] == '1':
                winner = 1
                y, x = i + 3, j + 3
            elif in_range4(j, i) and board[i + 1][j - 1] == '1' and board[i + 2][j - 2] == '1' and board[i + 3][j - 3] == '1' and board[i + 4][j - 4] == '1':
                winner = 1
                y, x = i + 3, j - 1

        elif board[i][j] == '2':
            if in_range1(j, i) and board[i + 1][j] == '2' and board[i + 2][j] == '2' and board[i + 3][j] == '2' and board[i + 4][j] == '2':
                winner = 2
                y, x = i + 3, j + 1
            elif in_range2(j, i) and board[i][j + 1] == '2' and board[i][j + 2] == '2' and board[i][j + 3] == '2' and board[i][j + 4] == '2':
                winner = 2
                y, x = i + 1, j + 3
            elif in_range3(j, i) and board[i + 1][j + 1] == '2' and board[i + 2][j + 2] == '2' and board[i + 3][j + 3] == '2' and board[i + 4][j + 4] == '2':
                winner = 2
                y, x = i + 3, j + 3
            elif in_range4(j, i) and board[i + 1][j - 1] == '2' and board[i + 2][j - 2] == '2' and board[i + 3][j - 3] == '2' and board[i + 4][j - 4] == '2':
                winner = 2
                y, x = i + 3, j - 1

print(winner)
if winner != 0:
    print(y, x)