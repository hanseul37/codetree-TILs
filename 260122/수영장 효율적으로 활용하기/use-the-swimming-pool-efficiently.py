n, m = map(int, input().split())
t = list(map(int, input().split()))

def check(limit):
    lane, cnt = 1, 0
    for time in t:
        if cnt + time > limit:
            lane += 1
            cnt = 0
        if lane > m:
            return False
        cnt += time
    return True

left, right = 0, 1440 * n
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)