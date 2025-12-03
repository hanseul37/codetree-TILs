from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
points = list(map(int, input().split()))

for _ in range(q):
    a, b = map(int, input().split())
    print(bisect_right(points, b) - bisect_left(points, a))

