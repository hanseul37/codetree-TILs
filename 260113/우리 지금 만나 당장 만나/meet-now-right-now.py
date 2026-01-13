n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

def check(time):
    l, r = -10 ** 9, 10 ** 9
    for i in range(n):
        l = max(x[i] - v[i] * time, l)
        r = min(x[i] + v[i] * time, r)
    return l <= r
      
left, right = 0, 10 ** 9
for _ in range(100):
    mid = (left + right) / 2
    if check(mid):
        right = mid 
    else:
        left = mid
print(f"{right:.4f}")
    