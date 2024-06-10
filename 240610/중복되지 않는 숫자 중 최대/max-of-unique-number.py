n = int(input())
arr = list(map(int, input().split()))
sum = []
cnt = 0
for i in range(n):
    if arr.count(arr[i]) < 2:
        sum.append(arr[i])
        cnt += 1

if len(sum) == 0:
    print(-1)
else:
    print(max(sum))