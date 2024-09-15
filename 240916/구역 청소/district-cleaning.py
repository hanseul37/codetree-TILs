a, b = map(int, input().split())
c, d = map(int, input().split())
if c <= b <= d:
    if c <= a <= d:
        print(d - c)
    else:
        print(b + d - a - c - (b - c))
elif a <= d <= b:
    if a <= c <= b:
        print(b - a)
    else:
        print(b + d - a - c - (d - a))
else:
    print(b + d - a - c)