def rect(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            if cnt == 10:
                cnt = 1
            print(cnt, end=" ")
            cnt += 1 
        print()
n = int(input())
rect(n)