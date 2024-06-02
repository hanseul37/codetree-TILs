n = int(input())
cnt = 1
for i in range(1, n+1):
    for j in range(1, i):
        print(' ', end=" ")
    for j in range(n-i+1):
        print(cnt, end=" ")
        if cnt == 9:
            cnt = 1
        else:
            cnt += 1
    print()