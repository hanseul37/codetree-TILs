n, k = map(int, input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))
bomb_count = {}

for i in range(n):
    type = bombs[i]
    if type not in bomb_count:
        bomb_count[type] = 0
    
    for j in range(i + 1, min(i + k + 1, n)):
        if bombs[j] == type:
            bomb_count[type] += 1
            bomb_count[bombs[j]] += 1

max_explosions = 0
max_type = 0

for type, count in bomb_count.items():
    if count > max_explosions or (count == max_explosions and type > max_type):
        max_explosions = count
        max_type = type

print(max_type)