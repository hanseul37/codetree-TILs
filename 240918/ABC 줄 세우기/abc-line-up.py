n = int(input())
arr = input().split()
sorted_arr = sorted(arr)
cnt = 0
point = n - 1

while point > 0:
    cnt += point - arr.index(sorted_arr[point])
    arr.remove(sorted_arr[point])
    arr.append(sorted_arr[point])
    point -= 1

print(cnt)