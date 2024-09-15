a, b = map(int, input().split())
c, d = map(int, input().split())
if c < b < d:
    print(b + d - a - c - (b - c))
elif a < d < b:
    print(b + d - a - c - (d - a))
else:
    print(b + d - a - c)