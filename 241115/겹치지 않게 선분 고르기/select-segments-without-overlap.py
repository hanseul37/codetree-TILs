n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:x[1])
max_cnt = 0
last_end = 0

for start, end in arr:
    if start > last_end:
        max_cnt += 1
        last_end = end
    
print(max_cnt)