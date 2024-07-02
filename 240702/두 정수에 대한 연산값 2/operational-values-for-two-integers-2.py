def change(a:int, b:int):
    if a > b:
        return a * 2, b + 10
    else:
        return a + 10, b * 2

a, b = list(map(int, input().split()))
a, b = change(a, b)
print(a, b)