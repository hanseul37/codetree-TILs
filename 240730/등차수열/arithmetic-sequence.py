n = int(input())
arr = list(map(int, input().split()))
max_cnt = 0
for i in range(101):
    cnt = 0
    for j in range(n - 1):
        for k in range(j + 1, n):
            if arr[j] - i == i - arr[k]:
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)