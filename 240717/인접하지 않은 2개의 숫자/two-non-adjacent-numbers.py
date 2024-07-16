import sys

n = int(input())
numbers = list(map(int, input().split()))

max = -sys.maxsize
for i in range(n - 1):
    for j in range(i + 1, n):
        if j - i == 1:
            continue
        if max < numbers[i] + numbers[j]:
            max = numbers[i] + numbers[j]
print(max)