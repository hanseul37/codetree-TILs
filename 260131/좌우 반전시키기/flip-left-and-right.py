n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n - 1):
    if arr[i] == 0:
        for j in range(3):
            arr[i + j] = (arr[i + j] + 1) % 2
        cnt += 1
if arr[-1] == 0:
    print(-1)
else:
    print(cnt)