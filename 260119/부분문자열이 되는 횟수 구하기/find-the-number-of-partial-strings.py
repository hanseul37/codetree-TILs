a = input()
b = input()
order = list(map(int, input().split()))
n, m = len(a), len(b)
alive = [0] * n
for i in range(n):
    alive[order[i] - 1] = i + 1

def check(time):
    point = -1
    for i in range(m):
        if point == n - 1:
            return False
        flag = False
        for j in range(point + 1, n):
            if a[j] == b[i] and alive[j] > time:
                point = j
                flag = True
                break
        if not flag:
            return False
    return True

left, right = 0, n
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(left)
        

