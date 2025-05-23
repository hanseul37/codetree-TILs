n = int(input())
arr = [0] * n
arr[0] = 1
for i in range(n - 3):
    arr[i + 2] += arr[i]
    arr[i + 3] += arr[i]
print((arr[n - 2] + arr[n - 3]) % 10007)