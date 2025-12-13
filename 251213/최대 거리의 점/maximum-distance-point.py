n, m = map(int, input().split())
points = [int(input()) for _ in range(n)]
points.sort()

def check(value):
    cnt, point = 0, -value
    for i in range(n):
        if points[i] - point >= value:
            cnt += 1
            point = points[i]
    if cnt >= m:
        return True
    else:
        return False

left, right = 1, points[-1] - points[0]
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)