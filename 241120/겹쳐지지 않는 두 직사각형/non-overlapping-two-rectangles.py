n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] 

max_sum = -1000 * n * m
for i in range(n):
    for j in range(m - 1):
        for k in range(n):
            for l in range(j + 1, m):
                for a in range(n - i):
                    for b in range(l - j):
                        for c in range(n - k):
                            for d in range(m - l):
                                cnt = 0
                                for e in range(i, i + a + 1):
                                    for f in range(j, j + b + 1):
                                        cnt += arr[e][f]
                                for e in range(k, k + c + 1):
                                    for f in range(l, l + d + 1):
                                        cnt += arr[e][f]
                                max_sum = max(max_sum, cnt)

for i in range(n - 1):
    for j in range(m):
        for k in range(i + 1, n):
            for l in range(m):
                for a in range(k - i):
                    for b in range(m - j):
                        for c in range(n - k):
                            for d in range(m - l):
                                cnt = 0
                                for e in range(i, i + a + 1):
                                    for f in range(j, j + b + 1):
                                        cnt += arr[e][f]
                                for e in range(k, k + c + 1):
                                    for f in range(l, l + d + 1):
                                        cnt += arr[e][f]
                                max_sum = max(max_sum, cnt)
print(max_sum)