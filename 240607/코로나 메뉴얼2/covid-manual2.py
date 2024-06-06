cnt = [0] * 4
for i in range(3):
    arr = input().split()
    a = arr[0]
    b = int(arr[1])
    if a == 'Y' and b >= 37:
        cnt[0] += 1
    elif a == 'N' and b >= 37:
        cnt[1] += 1
    elif a == 'Y' and b < 37:
        cnt[2] += 1
    else:
        cnt[3] += 1
for i in range(4):
    print(cnt[i], end=" ")
if cnt[0] >= 2:
    print('E')