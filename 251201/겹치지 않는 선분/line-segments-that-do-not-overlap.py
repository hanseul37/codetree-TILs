n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
left, right = [0] * n, [0] * n
arr.sort()

left[0], right[-1] = arr[0][1], arr[-1][1]
for i in range(1, n):
    left[i] = max(left[i - 1], arr[i][1])
    right[n - 1 - i] = min(right[n - i], arr[i][1])

cnt = 0
for i in range(n):
    if left[i] == right[i]:
        cnt += 1
print(cnt)