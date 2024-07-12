n, m = list(map(int, input().split()))
a, b = [], []
a_point, b_point = 0, 0
for _ in range(n):
    t, d = input().split()
    if d == 'L':
        for i in range(int(t)):
            a_point -= 1
            a.append(a_point)
    else:
        for i in range(int(t)):
            a_point += 1
            a.append(a_point)

for _ in range(m):
    t, d = input().split()
    if d == 'L':
        for i in range(int(t)):
            b_point -= 1
            b.append(b_point)
    else:
        for i in range(int(t)):
            b_point += 1
            b.append(b_point)

cnt = 0
if len(a) > len(b):
    max_len = len(a)
    min_len = len(b)
    b.append(b[min_len - 1])
elif len(a) < len(b):
    max_len = len(b)
    min_len = len(a)
    a.append(a[min_len - 1])

for i in range(max_len):
    if len(a) > len(b) and i > len(b) - 1:
        if a[i] == b[-1] and a[i - 1] != b[-2]:
            cnt += 1
    elif len(a) < len(b) and i > len(a) - 1:
        if a[-1] == b[i] and a[-2] != b[i - 1]:
            cnt += 1
    else:
        if a[i] == b[i] and a[i - 1] != b[i - 1]:
            cnt += 1

print(cnt)