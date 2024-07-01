def rect(n: int, m:int):
    for _ in range(n):
        for _ in range(m):
            print(1, end="")
        print()
n, m = list(map(int, input().split()))
rect(n, m)