arr = list(map(int, input().split()))
total = sum(arr)
min_diff = total
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            sum1 = arr[i] + arr[j] + arr[k]
            sum2 = total - sum1
            if abs(sum1 - sum2) < min_diff:
                min_diff = abs(sum1 - sum2)
print(min_diff)