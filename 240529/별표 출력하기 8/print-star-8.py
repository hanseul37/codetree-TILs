n = int(input())
for i in range(n):
    if (i + 1) % 2 == 0:
        for j in range(i+1):
            print('*', end=" ")
    else:
        print('*', end=" ")
    print()