n = int(input())
cnt = 0
for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(n):
            cnt += 1
            print(cnt, end=" ")
    else:
        cnt = cnt + n 
        for j in range(cnt, cnt-n, -1):
            print(j, end=" ")
    print()