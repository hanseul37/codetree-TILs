N, K = list(map(int, input().split()))
arr = [0 for i in range(N)]
for i in range(K):
    a, b = list(map(int, input().split()))
    for j in range(a, b + 1):
        arr[j - 1] += 1
print(max(arr))