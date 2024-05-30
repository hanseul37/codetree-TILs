n = int(input())
for i in range(n):
    for j in range(n):
        if j == n-1 or i == 0 or i > j:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()