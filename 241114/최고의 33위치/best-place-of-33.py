n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_cnt = 0
for i in range(1, n - 1):
    for j in range(1, n-1):
        cnt = 0
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                if arr[k][l] == 1:
                    cnt+=1
        max_cnt = max(max_cnt, cnt)
print(max_cnt)