n = int(input())
arr = list(input())
max_cnt = 0

for i in range(n):
    min_cnt = n
    if arr[i] == '1':
        continue
    else:
        copy_arr = arr.copy()
        copy_arr[i] = '1'
        cnt = 0
        for j in range(1, n):
            if j == n - 1:
                if copy_arr[j] == '0':
                    cnt += 1
                min_cnt = min(min_cnt, cnt)
                cnt = 0
            elif j == 0 and copy_arr[j] == '1':
                continue
            elif copy_arr[j] == '0':
                cnt += 1
            else:
                min_cnt = min(min_cnt, cnt)
                cnt = 0
    max_cnt = max(max_cnt, min_cnt)
print(max_cnt + 1)