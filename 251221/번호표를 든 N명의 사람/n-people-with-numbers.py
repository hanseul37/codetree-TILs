import heapq

n, t = map(int, input().split())
d = [int(input()) for _ in range(n)]

def check(num):
    q = d[:num]
    heapq.heapify(q)
    idx, time = num, 0
    while idx < n:
        out = heapq.heappop(q)
        time = out
        heapq.heappush(q, time + d[idx])
        idx += 1
        if time > t:
            return False
    if max(q) <= t:
        return True
    else:
        return False

left, right = 1, n
while left <= right:
    mid = (left + right) // 2
    if not check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(left)
