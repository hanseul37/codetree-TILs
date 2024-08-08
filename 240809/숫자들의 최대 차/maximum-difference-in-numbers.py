n, k = map(int, input().split())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

max_cnt = 0
for i in range(11001):
    cnt = 0
    for j in range(n):
        if i <= arr[j] <= i + k:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)