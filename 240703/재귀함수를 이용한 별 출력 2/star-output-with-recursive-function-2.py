def star(n: int):
    if n == 0:
        return
    for _ in range(n):
        print('*', end=" ")
    print()
    star(n - 1)
    for _ in range(n):
        print('*', end=" ")
    print()

n = int(input())
star(n)