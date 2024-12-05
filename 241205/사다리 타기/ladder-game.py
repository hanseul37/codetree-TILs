n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
answer = [i for i in range(n)]

arr = sorted(arr, key=lambda x: x[1])
for i in range(m):
    temp = answer[arr[i][0] - 1]
    answer[arr[i][0] - 1] = answer[arr[i][0]]
    answer[arr[i][0]] = temp
    
cnt = 0
for i in range(n):
    if answer[i] - i > 0:
        cnt += answer[i] - i

print(cnt)