k, n = map(int, input().split())

def pick(num):
    if len(num) == n:
        for i in range(n):
            print(num[i], end=' ')
        print()
        return
    for i in range(1, k + 1):
        if len(num) >= 2 and num[-1] == i and num[-2] == i:
            continue
        num.append(i)
        pick(num)
        num.pop()

pick([])
