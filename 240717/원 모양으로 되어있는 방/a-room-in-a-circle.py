import sys

n = int(input())
arr = []
for _ in range(n):
    limit = int(input())
    arr.append(limit)

min = sys.maxsize
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[j] * ((j - i) % n)
    if min > sum:
        min = sum

print(min)