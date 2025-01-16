k, n = map(int, input().split())

def pick(num):
    if len(num) == n:
        for i in range(n):
            print(num[i], end=' ')
        print()
        return
    for i in range(1, k + 1):
        if num.count(i) == 2:
            continue
        num.append(i)
        pick(num)
        num.pop()

pick([])
