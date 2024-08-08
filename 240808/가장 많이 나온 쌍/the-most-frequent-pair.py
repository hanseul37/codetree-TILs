n, m = map(int, input().split())
pair_count = {}

for _ in range(m):
    a, b = map(int, input().split())
    pair = (min(a, b), max(a, b))
    if pair in pair_count:
        pair_count[pair] += 1
    else:
        pair_count[pair] = 1

max_count = max(pair_count.values())
print(max_count)