arr = list(map(int, input().split()))
for i in arr:
    if i == 0:
        break
    else:
        if i % 2 == 0:
            i //= 2
        else:
            i += 3
        print(i, end=" ")