def check(n:str):
    return '3' in n or '6' in n or '9' in n

def three(n:int):
    return check(str(n))

def game(a:int, b:int):
    cnt = 0
    for i in range(a, b+1):
        if three(i) or i % 3 == 0:
            cnt += 1
    return cnt

a, b = list(map(int, input().split()))
ans = game(a, b)
print(ans)