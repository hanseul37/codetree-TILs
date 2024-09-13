n, m = map(int, input().split())
arr = list(map(int, input().split()))

def can_divide(arr, m, max_sum):
    cur_sum = 0
    cnt = 1
    for num in arr:
        if cur_sum + num > max_sum:
            cnt += 1
            cur_sum = num  
            if cnt > m:
                return False
        else:
            cur_sum += num 
    return True

max_arr = max(arr)
sum_arr = sum(arr)
while max_arr < sum_arr:
    mid = (max_arr + sum_arr) // 2
    if can_divide(arr, m, mid):
        sum_arr = mid
    else:
        max_arr = mid + 1
print(max_arr)