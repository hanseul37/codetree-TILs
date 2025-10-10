n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def check(num):
    cnt = 0
    for elem in arr:
        cnt += elem // num
    return cnt

left, right = 1, max(arr)
while left <= right:
    mid = (left + right) // 2
    if check(mid) >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)

