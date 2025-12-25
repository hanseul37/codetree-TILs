n = int(input())
numbers = [int(input()) for _ in range(n)]
prefix = [0]
for i in range(n):
    prefix.append(prefix[i] + numbers[i])
max_value = 0
for i in range(1, n + 1):
    for j in range(i):
        value = prefix[i] - prefix[j]
        if value % 7 == 0:
            max_value = max(i - j, max_value)
print(max_value)