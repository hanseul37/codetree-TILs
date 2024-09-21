n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

avg = sum(arr) // n

cnt = 0
for i in range(n):
    if arr[i] < avg:
        cnt += avg - arr[i]
print(cnt)