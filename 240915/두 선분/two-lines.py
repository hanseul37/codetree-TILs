x1, x2, x3, x4 = map(int, input().split())
if x3 <= x2 <= x4 or x1 <= x4 <= x2:
    print('intersecting')
else:
    print('nonintersecting')