n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

def check(num):
    idx, cnt, point = 0, 1, arr[0][0]
    while idx < m:
        if point + num <= arr[idx][1]:
            cnt += 1
            point += num
        else:
            idx += 1
        if cnt >= n:
            return True
    return False

left, right = 1, 10 ** 18 // n
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)
