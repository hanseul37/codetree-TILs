def mini(n:int, m:int):
    for i in range(max(n, m), n * m, max(n, m)):
        if i % min(n, m) == 0:
            print(i)
            break
n, m = list(map(int, input().split()))
mini(n, m)