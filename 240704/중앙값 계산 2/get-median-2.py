n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if i % 2 == 0:
        new_arr = arr[:i+1]
        new_arr.sort()
        print(new_arr[((len(new_arr) - 1) // 2)], end=' ')