n, k = list(map(int, input().split()))
bombs = []
for _ in range(n):
    bomb = int(input())
    bombs.append(bomb)

num = -1
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif abs(i - j) <= k and bombs[i] == bombs[j]:
            num = max(num, bombs[i])
print(num)