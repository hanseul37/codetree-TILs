import copy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n):
    for j in range(n):
        copy_arr = copy.deepcopy(arr)
        for k in range(copy_arr[i][j]):
            if i - k >= 0:
                copy_arr[i - k][j] = 0
            if i + k < n:
                copy_arr[i + k][j] = 0
            if j - k >= 0:
                copy_arr[i][j - k] = 0
            if j + k < n:
                copy_arr[i][j + k] = 0
        for k in range(n):
            non_zero = []
            for l in range(n):
                if copy_arr[l][k] != 0:
                    non_zero.append(copy_arr[l][k])
            for l in range(n - len(non_zero)):
                copy_arr[l][k] = 0
            for l in range(n - len(non_zero), n):
                copy_arr[l][k] = non_zero[l - n + len(non_zero)]

        cnt = 0
        for k in range(n):
            for l in range(n):
                if copy_arr[k][l] == 0:
                    continue
                if k + 1 < n and copy_arr[k][l] == copy_arr[k + 1][l]:
                    cnt += 1
                if l + 1 < n and copy_arr[k][l] == copy_arr[k][l + 1]:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)        

print(max_cnt)
