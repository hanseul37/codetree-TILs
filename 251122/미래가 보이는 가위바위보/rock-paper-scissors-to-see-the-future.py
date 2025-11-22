n = int(input())
b = [input() for _ in range(n)]
a_left, a_right = [[0] * n for _ in range(3)], [[0] * n for _ in range(3)]
op = ['S', 'H', 'P']
for i in range(len(op)):        
    if op[i] == b[0]:
        a_left[i][0] += 1
    if op[i] == b[-1]:
        a_right[i][-1] += 1
    for j in range(1, n):
        a_left[i][j] = a_left[i][j - 1]
        a_right[i][n - 1 - j] = a_right[i][n - j]
        if op[i] == b[j]:
            a_left[i][j] += 1
        if op[i] == b[n - 1 - j]:
            a_right[i][n - 1 - j] += 1

max_win = 0
for i in range(3):
    for j in range(3):
        for k in range(n - 1):
            max_win = max(a_left[i][k] + a_right[j][k + 1], max_win)
print(max_win)
 


