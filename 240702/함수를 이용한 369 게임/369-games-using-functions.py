def check(n:int):
    return n == 3 or n == 6 or n == 9

def three(n:int):
    a = n // 10
    b = n % 10
    return check(a) or check(b)

def game(a:int, b:int):
    cnt = 0
    for i in range(a, b+1):
        if three(i) or i % 3 == 0:
            cnt += 1
    return cnt

a, b = list(map(int, input().split()))
ans = game(a, b)
print(ans)