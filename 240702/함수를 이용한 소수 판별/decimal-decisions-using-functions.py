def prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = list(map(int, input().split()))
sum = 0
for i in range(a, b+1):
    if prime(i):
        sum += i
print(sum)