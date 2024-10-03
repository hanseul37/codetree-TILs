n = int(input())
arr = list(map(int, input().split()))
min_cnt = n
for i in range(n - 1, -1, -1):
    temp = arr[i:]
    if temp != sorted(temp):
        min_cnt = i + 1
        break
if arr == sorted(arr):
    min_cnt = 0
print(min_cnt)