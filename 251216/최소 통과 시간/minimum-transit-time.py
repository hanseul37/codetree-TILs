n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

def check(num):
    cnt = 0
    for pipe in arr:
        cnt += num // pipe
    if cnt >= n:
        return True
    else:
        return False

left, right = 1, 100000
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)