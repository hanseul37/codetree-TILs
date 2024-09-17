a, b, c = map(int, input().split())
if a + 1 == b and b + 1 == c:
    print(0)
elif a + 2 == b or b + 2 == c:
    print(1)
elif a + 3 == b or b + 3 == c:
    print(2)
else:
    print(3)