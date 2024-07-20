n, k = list(map(int, input().split()))
arr = [0] * 101
for _ in range(n):
    candy, bucket = list(map(int, input().split()))
    arr[bucket] = candy

max_candy = 0
for i in range(k, 101 - k):
    sum = 0
    for j in range(i - k, i + k + 1):
        sum += arr[j]
    if sum > max_candy:
        print(i)
    max_candy = max(max_candy, sum)

print(max_candy)