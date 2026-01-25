n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    for _ in range(x):
        arr.append(y)
arr.sort()
c = 10 ** 9 * 2
for i in range(len(arr) // 2):
    c = min(arr[i] + arr[len(arr) - 1 - i], c)
print(c)