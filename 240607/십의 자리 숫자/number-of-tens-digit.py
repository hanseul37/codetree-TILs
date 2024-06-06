arr = list(map(int, input().split()))
cnt = [0] * 10
for i in arr:
    if i == 0:
        break
    cnt[i//10] += 1
for i in range(1, 10):
    print(f'{i} - {cnt[i]}')