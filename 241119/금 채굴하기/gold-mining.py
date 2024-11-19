n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_benefit = 0
max_gold = 0
for i in range(n):
    for j in range(n):
        for k in range(2 * n):
            gold = 0
            for a in range(n):
                for b in range(n):
                    if arr[a][b] == 1 and abs(i - a) + abs(j - b) <= k:
                        gold += 1
            benefit = gold * m - (k * k + (k + 1) * (k + 1))
            if benefit >= 0:
                max_benefit = max(max_benefit, benefit)
                max_gold = max(max_gold, gold)
print(max_gold)

