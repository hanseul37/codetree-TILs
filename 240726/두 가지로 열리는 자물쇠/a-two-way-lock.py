n = int(input())
a1, b1, c1 = list(map(int, input().split()))
a2, b2, c2 = list(map(int, input().split()))
a1, b1, c1 = a1 - 1, b1 - 1, c1 - 1
a2, b2, c2 = a2 - 1, b2 - 1, c2 - 1

def near(x, y, n):
    return min((x - y) % n, (y - x) % n) <= 2

cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (near(i, a1, n) and near(j, b1, n) and near(k, c1, n)) or (near(i, a2, n) and near(j, b2, n) and near(k, c2, n)):
                cnt += 1
print(cnt)