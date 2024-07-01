def cal(n:int, m:int):
    big = 1
    if n > m:
        for i in range(2, m + 1):
            if n % i == 0 and m % i ==0:
                big = i
    else:
        for i in range(2, n + 1):
            if n % i == 0 and m % i == 0:
                big = i
    print(big)

n, m = list(map(int, input().split()))
cal(n,m)