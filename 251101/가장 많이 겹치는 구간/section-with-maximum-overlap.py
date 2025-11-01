n = int(input())
check = [0] * 200001
for _ in range(n):
    x1, x2 = map(int, input().split())
    check[x1] += 1
    check[x2] -= 1

max_cnt, cnt = 0, 0
for elem in check:
    cnt += elem
    max_cnt = max(cnt, max_cnt)

print(max_cnt)