n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: -(x[1] / x[0]))
capacity, cnt = m, 0
for w, v in arr:
    if capacity == 0:
        break
    if w <= capacity:
        cnt += v
        capacity -= w
    else:
        cnt += v * (capacity / w)
        capacity = 0
print(f"{cnt:.3f}")