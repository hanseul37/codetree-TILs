n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] + arr[j] <= k:
            cnt += 1
        else:
            break
print(cnt) 


