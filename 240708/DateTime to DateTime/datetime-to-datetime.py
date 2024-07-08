a, b, c = list(map(int, input().split()))
if a == 11:
    if b < 11:
        print(-1)
    elif b == 11:
        if c < 11:
            print(-1)
        else:
            print(c - 11)
    else:
        print((b - 11) * 60 + c - 11)
else:
    print((a - 11) * 1440 + (b - 11) * 60 + c - 11)