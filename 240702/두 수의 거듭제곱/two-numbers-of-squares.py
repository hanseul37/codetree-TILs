def square(a:int, b:int):
    n = 1
    for _ in range(b):
        n *= a
    return n

a, b = list(map(int, input().split()))
print(square(a, b))