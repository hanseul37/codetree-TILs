from math import comb

n = int(input())
arr = list(map(int, input().split()))
prefix, left, right = [0] * n, [0] * n, [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

total = prefix[-1]
t1, t2, t3 = total // 4, total // 4 * 2, total // 4 * 3
if total == 0:
    print(comb(n - 1, 3))
    exit()

l_cnt, r_cnt = 0, 0
for i in range(n):
    if prefix[i] == t1:
        l_cnt += 1
    if prefix[n - 1 - i] == t3:
        r_cnt += 1
    left[i], right[n - 1 - i] = l_cnt, r_cnt

cnt = 0
for i in range(n):
    if prefix[i] == t2:
        cnt += left[i] * right[i]
print(cnt)