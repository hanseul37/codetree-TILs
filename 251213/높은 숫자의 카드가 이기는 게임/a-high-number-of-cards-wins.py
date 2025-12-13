n = int(input())
b = [int(input()) for _ in range(n)]
total = set(range(1, 2 * n + 1))
a = sorted(total - set(b))
b.sort(reverse = True)
cnt, a_idx = 0, n - 1
for b_card in b:
    if a_idx >= 0 and a[a_idx] > b_card:
        cnt += 1
        a_idx -= 1
print(cnt)
            

