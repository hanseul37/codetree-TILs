n, t = list(map(int, input().split()))
arr = list(map(int, input().split()))

max, cnt = 0, 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
        if max < cnt:
            max = cnt
    else:
        cnt = 0

print(max)