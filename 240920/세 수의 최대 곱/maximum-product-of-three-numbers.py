n = int(input())
arr = list(map(int, input().split()))
cnt = 0
max_value = -1000
if max(arr) < 0 or min(arr) > 0:
    copy_arr = sorted(arr)
    max_value = copy_arr[-1] * copy_arr[-2] * copy_arr[-3]
else:
    for i in range(n - 2):
        if arr[i] == 0:
            continue
        elif arr[i] < 0:
            cnt += 1

        for j in range(i + 1, n - 1):
            if arr[j] == 0:
                continue
            elif arr[i] < 0:
                cnt += 1

            for k in range(j + 1, n):
                if arr[k] == 0:
                    continue
                elif arr[k] < 0 and (cnt == 0 or cnt == 2):
                    continue
                elif arr[k] > 0 and cnt == 1:
                    continue
                else:
                    max_value = max(max_value, arr[i] * arr[j] * arr[k])
    max_value = max(max_value, 0)

print(max_value)