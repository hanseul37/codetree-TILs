n = int(input())
events = []

for _ in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))   # 시작
    events.append((r, -1))  # 끝

events.sort()

cur = 0
answer = 0

for _, v in events:
    cur += v
    answer = max(answer, cur)

print(answer)
