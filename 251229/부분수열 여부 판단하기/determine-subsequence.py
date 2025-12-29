n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_idx, b_idx, ans = 0, 0, 'No'

while a_idx < n and b_idx < m:
    if a[a_idx] == b[b_idx]:
        b_idx += 1
    a_idx += 1
    if b_idx == m:
        ans = 'Yes'
        break 

print(ans)