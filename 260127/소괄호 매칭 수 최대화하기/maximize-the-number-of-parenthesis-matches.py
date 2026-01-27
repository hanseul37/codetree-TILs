n = int(input())
arr, ans = [], 0
for i in range(n):
    s = input()
    cnt = 0
    for elem in s:
        if elem == '(':
            cnt += 1
        else:
            ans += cnt
    arr.append([s.count('('), s.count(')')])

for i in range(n):
    for j in range(i + 1, n):
        if arr[i][0] * arr[j][1] < arr[j][0] * arr[i][1]:
            arr[i], arr[j] = arr[j], arr[i]

point = 0
for a, b in arr:   
    ans += point * b
    point += a
print(ans)
