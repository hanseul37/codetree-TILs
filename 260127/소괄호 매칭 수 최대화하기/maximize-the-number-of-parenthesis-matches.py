from functools import cmp_to_key

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

def cmp(x, y):
    return y[0] * x[1] - x[0] * y[1]

arr.sort(key=cmp_to_key(cmp))

point = 0
for a, b in arr:   
    ans += point * b
    point += a
print(ans)
