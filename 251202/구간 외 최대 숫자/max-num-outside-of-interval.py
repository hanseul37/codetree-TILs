n, q = map(int, input().split())
arr = list(map(int, input().split()))
left, right = [0] * n, [0] * n
left[0], right[-1] = arr[0], arr[-1]
for i in range(1, n):
    left[i] = max(left[i - 1], arr[i])
    right[n - 1 - i] = max(right[n - i], arr[n - 1 - i])

for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(max(left[a - 1], right[b + 1]))