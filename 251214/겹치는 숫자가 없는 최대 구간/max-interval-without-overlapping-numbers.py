n = int(input())
arr = list(map(int, input().split()))
count = {}
j, max_cnt = 0, 0
for i in range(n):
    while j + 1 < n and (arr[j] not in count or count[arr[j]] == 0):
        if arr[j] in count:
            count[arr[j]] += 1
        else:
            count[arr[j]] = 1
        j += 1
    max_cnt = max(j - i, max_cnt)
    count[arr[i]] -= 1
print(max_cnt)

