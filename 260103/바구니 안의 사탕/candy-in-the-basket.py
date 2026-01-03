n, k = map(int, input().split())
buckets = [list(map(int, input().split())) for _ in range(n)]
buckets.sort(key=lambda x:x[1])
left, window, max_candy = 0, 0, 0
for right in range(n):
    window += buckets[right][0]
    while buckets[right][1] - buckets[left][1] > 2 * k:
        window -= buckets[left][0]
        left += 1
    max_candy = max(window, max_candy)
print(max_candy)