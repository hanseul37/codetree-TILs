n = int(input())
for i in range(0, n):
    for j in range(i, n):
        print('*', end = " ")
    print()
for i in range(2, n+1):
    for j in range(0, i):
        print('*', end = " ")
    print()