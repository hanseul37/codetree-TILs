def prime(n:int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def location(n:int):
    total = sum(int(i) for i in str(n))
    return total % 2 == 0

def check(a:int, b:int):
    cnt = 0
    for i in range(a, b+1):
        if prime(i) and location(i):
            cnt += 1
    return cnt

a, b = list(map(int, input().split()))
print(check(a, b))