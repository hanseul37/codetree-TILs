n = int(input())
arr = list(map(int, input().split()))
min_cnt = n
for i in range(n - 1, -1, -1):
    temp = arr[i:]
    if temp != sorted(temp):
        min_cnt = i
        break
print(min_cnt + 1)