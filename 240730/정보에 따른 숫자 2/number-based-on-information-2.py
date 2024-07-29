t, a, b = list(map(int, input().split()))
alphabet = [''] * 1001
for _ in range(t):
    alpha, location = input().split()
    alphabet[int(location)] = alpha

cnt = 0
for i in range(a, b + 1):
    n_dist, s_dist = 1000, 1000
    for j in range(1001):
        if alphabet[j] == 'N':
            if abs(i - j) < n_dist:
                n_dist = abs(i - j)
        elif alphabet[j] == 'S':
            if abs(i - j) < s_dist:
                s_dist = abs(i - j)
    if n_dist >= s_dist:
        cnt += 1
print(cnt)