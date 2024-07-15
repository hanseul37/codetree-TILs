import sys

n = int(input())
house = list(map(int, input().split()))
min = sys.maxsize
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(j - i) * house[j]
    if sum < min:
        min = sum

print(min)