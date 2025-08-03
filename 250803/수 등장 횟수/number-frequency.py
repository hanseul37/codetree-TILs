n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))
dic = {}
for i in range(n):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

for i in range(m):
    if nums[i] in dic:
        print(dic[nums[i]], end=' ')
    else:
        print('0', end=' ')

