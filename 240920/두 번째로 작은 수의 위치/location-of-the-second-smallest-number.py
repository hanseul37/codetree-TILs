n = int(input())
arr = list(map(int, input().split()))
copy_arr = sorted(arr)
find = 0
index = -1
second = -1
for i in range(n):
    if copy_arr[i] != copy_arr[0]:
        second = copy_arr[i]
        break

for i in range(n):
    if second == arr[i]:
        find += 1
        index = i + 1

if find > 1:
    print(-1)
else:
    print(index)