n = int(input())
arr = list(map(int, input().split()))
count = {}
j, max_cnt = 0, 0
for i in range(n):
    while j < n and arr[j] not in count:
        count[arr[j]] = 1
        j += 1
    max_cnt = max(j - i, max_cnt)
    del count[arr[i]]
print(max_cnt)

