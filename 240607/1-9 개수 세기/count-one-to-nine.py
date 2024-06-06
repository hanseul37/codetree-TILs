n = int(input())
arr = list(map(int, input().split()))
count = [0] * 9
for i in arr:
    count[i-1] += 1
for i in range(9):
    print(count[i])