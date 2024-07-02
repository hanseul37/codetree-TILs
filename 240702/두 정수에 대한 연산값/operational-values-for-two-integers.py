def change(a:int, b:int):
    if a > b:
        return a + 25, b * 2
    else:
        return a * 2, b + 25

a, b = list(map(int, input().split()))
a, b = change(a, b)
print(a, b)