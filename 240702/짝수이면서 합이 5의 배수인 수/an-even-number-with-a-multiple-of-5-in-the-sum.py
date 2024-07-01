def check(n:int):
    return n % 2 == 0 and (n // 10 + n % 10) % 5 == 0

n = int(input())
if check(n):
    print('Yes')
else:
    print('No')