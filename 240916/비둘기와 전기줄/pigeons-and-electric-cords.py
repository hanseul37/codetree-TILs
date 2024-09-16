n = int(input())
arr = [-1] * 10
cnt = 0
for i in range(n):
    pigeon, location = map(int, input().split())
    if arr[pigeon - 1] == -1:
        arr[pigeon - 1] = location
    elif arr[pigeon - 1] != location:
        cnt += 1
        arr[pigeon - 1] = location
print(cnt)