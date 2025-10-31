n, k, b = map(int, input().split())
missing = [int(input()) for _ in range(b)]
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    if i in missing:
        prefix[i] = prefix[i - 1] + 1
    else:
        prefix[i] = prefix[i - 1]

min_cnt = n
for i in range(n + 1 - k):
    min_cnt = min(prefix[i + k] - prefix[i], min_cnt)
print(min_cnt) 