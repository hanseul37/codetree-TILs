n = int(input())
bombs = [list(map(int, input().split())) for _ in range(n)]
bombs.sort(key=lambda x:(x[1], -x[0]))
time, total = 0, 0
for point, limit in bombs:
    if time < limit:
        total += point
        time += 1
print(total)

