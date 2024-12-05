from itertools import combinations

def simulate_ladder(ladder):
    answer = [i for i in range(n)]
    for a, b in sorted(ladder, key=lambda x: x[1]):
        answer[a - 1], answer[a] = answer[a], answer[a - 1]
    return answer

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

result = simulate_ladder(arr)

cnt = m
for line in range(m + 1):
    for subset in combinations(arr, line):
        if simulate_ladder(subset) == result:
            cnt = min(cnt, line)

print(cnt)
