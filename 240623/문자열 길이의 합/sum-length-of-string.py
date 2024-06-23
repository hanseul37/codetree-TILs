n = int(input())
arr = [
    input()
    for _ in range(n)
]
length = 0
for i in range(n):
    length += len(arr[i])
cnt = 0
for i in range(n):
    if arr[i][0] == 'a':
        cnt += 1
print(length, cnt)