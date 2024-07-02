def star(n:int):
    if n == 0:
        return
    star(n - 1)
    for _ in range(n):
        print('*', end='')
    print()

n = int(input())
star(n)