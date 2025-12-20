n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

def check(num):
    idx, point = 0, arr[0][0]
    while idx < n - 1:
        if point + num > arr[idx + 1][1]:
            return False
        else:
            point = max(point + num, arr[idx + 1][0])
            idx += 1
    return True

left, right = 1, 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)
