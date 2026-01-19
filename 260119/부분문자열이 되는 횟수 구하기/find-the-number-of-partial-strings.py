a = input()
b = input()
order = list(map(int, input().split()))
n, m = len(a), len(b)
alive = [0] * n
for i in range(n):
    alive[order[i] - 1] = i + 1

def check(time):
    idx = 0
    for i in range(n):
        if alive[i] > time and a[i] == b[idx]:
            idx += 1
            if idx == m:
                return True
    return False

left, right = 0, n
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(left)
        

