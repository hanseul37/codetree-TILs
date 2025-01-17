n, m, k = map(int, input().split())
num = list(map(int, input().split()))
max_point = 0

def game(location, cnt):
    global max_point
    if cnt == n:
        max_point = max(max_point, sum(1 for x in location if x >= m - 1))
        return
    for i in range(k):
        location[i] += num[cnt]
        game(location, cnt + 1)
        location[i] -= num[cnt]

game([0] * k, 0)
print(max_point)