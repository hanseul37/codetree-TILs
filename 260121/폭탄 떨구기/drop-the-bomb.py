n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

def check(r):
    idx, cnt = 0, 0
    while idx < n:
        cnt += 1
        cover = x[idx] + 2 * r
        while idx < n and x[idx] <= cover:
            idx += 1
        if cnt > k:
            return False
    return True

left, right = 0, 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)