n = int(input())
arr = list(input())
end = 0
max_cnt = 0
cnt = 0
for i in range(1, n):
    if arr[i] == '0':
        cnt += 1
    else:
        if max_cnt < cnt:
            end = i
            max_cnt = cnt
        cnt = 0

arr[end - (max_cnt // 2 + 1)] = '1'

min_cnt = n
cnt = 0
for i in range(1, n):
    if arr[i] == '0':
        cnt += 1
    else:
        min_cnt = min(min_cnt, cnt)
        cnt = 0

print(min_cnt + 1)