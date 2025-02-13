n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_value = 10000 * n * n
ans = [0]

def move():
    global min_value

    if len(ans) == n:
        value = 0
        for i in range(n - 1):
            value += arr[ans[i]][ans[i + 1]]
        value += arr[ans[-1]][0]
        min_value = min(min_value, value)

    for i in range(1, n):
        if i not in ans and arr[ans[-1]][i] != 0:
            ans.append(i)
            move()
            ans.pop()

move()
print(min_value)