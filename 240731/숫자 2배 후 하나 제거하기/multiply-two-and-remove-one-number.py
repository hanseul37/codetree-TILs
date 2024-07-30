n = int(input())
arr = list(map(int, input().split()))

min_diff = 10000
for i in range(n):
    for j in range(n):
        diff = 0
        new_arr = arr.copy()
        new_arr[i] *= 2
        del new_arr[j]
        for k in range(n - 2):
            diff += abs(new_arr[k] - new_arr[k + 1])            
        min_diff = min(min_diff, diff)

print(min_diff)