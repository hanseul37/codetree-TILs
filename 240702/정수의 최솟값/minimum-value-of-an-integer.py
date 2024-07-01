def mini(a:int, b:int, c:int):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
a, b, c = list(map(int, input().split()))
min = mini(a, b, c)
print(min)