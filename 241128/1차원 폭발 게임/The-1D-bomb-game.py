n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

i, cnt, flag = 0, 0, 0
point = arr[0]
while True:
    if len(arr) == 0:
        break

    if arr[i] == point:
        cnt += 1
        i += 1
    else:
        point = arr[i]
        if cnt >= m:
            arr = arr[:i - cnt] + arr[i:]
            flag = 1
            i = i - cnt
        i += 1
        cnt = 1

    if i >= len(arr):
        if flag == 0:
            break
        else:
            if cnt >= m:
                arr = arr[:len(arr) - cnt]
                flag = 1
                continue
            i = 0
            cnt = 0
            point = arr[0]
            flag = 0

if cnt >= m:
    arr = arr[:len(arr) - cnt]

print(len(arr))
for i in range(len(arr)):
    print(arr[i])