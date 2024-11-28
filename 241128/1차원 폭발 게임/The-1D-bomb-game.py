n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

i, cnt = 0, 0
point = arr[0]
while True:
    if arr[i] == point:
        cnt += 1
        i += 1
    else:
        if cnt >= m:
            arr = arr[:i] + arr[i + cnt:]
            i = 0
            point = arr[0]
        else:
            point = arr[i]
            i += 1
        cnt = 1
    if i >= len(arr):
        break
if cnt >= m:
    arr = arr[:len(arr) - cnt]

print(len(arr))
for i in range(len(arr)):
    print(arr[i])