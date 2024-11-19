n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def check(x, y):
    return 0 <= x < n and 0 <= y < n 

max_cnt = 0
for i in range(2, n):
    for j in range(1, n - 1):
        for k in range(1, n - 1):
            for l in range(1, n - 1):
                if (check(j + k, i - k) and  
                    check(j + k - l, i - k - l) and  
                    check(j - l, i - l)):  
                    flag = 0
                    cnt = 0
                    for a in range(1, k + 1):
                        if check(j + a, i - a):
                            cnt += arr[i - a][j + a]
                        else:
                            flag = 1
                    for a in range(1, l + 1):
                        if check(j + k - a, i - k - a):
                            cnt += arr[i - k - a][j + k - a]
                        else:
                            flag = 1
                    for a in range(1, k + 1):
                        if check(j + k - l - a, i - k - l + a):
                            cnt += arr[i - k - l + a][j + k - l - a]
                        else:
                            flag = 1
                    for a in range(1, l + 1):
                        if check(j - l + a, i - l + a):
                            cnt += arr[i - l + a][j - l + a]
                        else:
                            flag = 1
                    if flag == 0:
                        max_cnt = max(max_cnt, cnt)
print(max_cnt)