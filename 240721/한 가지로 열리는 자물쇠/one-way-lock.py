n = int(input())
a, b, c = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if abs(a - i - 1) <= 2 or abs(b - j - 1) <= 2 or abs(c - k - 1) <= 2:
                cnt += 1
print(cnt)