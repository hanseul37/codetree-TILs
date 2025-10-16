n = int(input())

def check(num):
    return num - num // 3 - num // 5 + num // (3 * 5)

left, right = 0, n * 2
while left <= right:
    mid = (left + right) // 2
    if check(mid) > n:
        right = mid - 1
    else:
        left = mid + 1
print(right)