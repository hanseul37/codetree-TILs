from math import comb

n = int(input())
arr = list(map(int, input().split()))

if sum(arr) == 0:
    print(comb(n - 1, 3))
    exit()

prefix, left, right = [0] * n, [0] * n, [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

l_cnt, r_cnt = 0, 0
for i in range(n):
    if prefix[i] == sum(arr) // 4:
        l_cnt += 1
    if prefix[n - 1 - i] == sum(arr) // 4 * 3:
        r_cnt += 1
    left[i], right[i] = l_cnt, r_cnt

cnt = 0
for i in range(n):
    if prefix[i] == sum(arr) // 2:
        cnt += left[i] * right[i]
print(cnt)