n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(len(a) - len(b) + 1):
    a_arr = sorted(a[i:i + len(b)])
    b_arr = sorted(b)
    flag = 0
    for j in range(len(b)):
        if a_arr[j] != b_arr[j]:
            flag = 1
            break
    if flag == 0:
        cnt += 1
print(cnt)