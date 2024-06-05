arr = list(map(int, input().split()))
su = 0
cnt = 0
for i in range(10):
    if i % 3 == 2:
        su += arr[i]
        cnt += 1
print(f'{sum(arr[1::2])} {su/cnt:.1f}')