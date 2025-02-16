n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_value = 0
printing = []

def find():
    global max_value

    if len(printing) == n:
        value = 10000
        for i in range(n):
            value = min(arr[i][printing[i]], value)
        max_value = max(max_value, value)

    for i in range(n):
        if i not in printing:
            printing.append(i)
            find()
            printing.pop()

find()
print(max_value)