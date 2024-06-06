n = int(input())
i = 1
cnt = 0
while True:
    if i * n % 5 == 0:
        cnt += 1
    print(i * n, end =" ")
    i += 1
    if cnt == 2:
        break