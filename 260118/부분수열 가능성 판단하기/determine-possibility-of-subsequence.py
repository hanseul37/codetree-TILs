n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
left, right = [-1] * m, [-1] * m
l_idx, r_idx = 0, n - 1
for i in range(m):
    while l_idx < n and a[l_idx] != b[i]:
        l_idx += 1
    if l_idx >= n:
        break
    left[i] = l_idx
    l_idx += 1

for i in range(m - 1, -1, -1):
    while r_idx > -1 and a[r_idx] != b[i]:
        r_idx -= 1
    if r_idx < 0:
        break
    right[i] = r_idx
    r_idx -= 1

cnt = 0
for i in range(m):
    if i > 0 and left[i - 1] == -1:
        continue
    if i < m - 1 and right[i + 1] == n:
        continue
    l = left[i - 1] if i > 0 else -1
    r = right[i + 1] if i < m - 1 else n
    if l < r:
        cnt += 1
print(cnt)    