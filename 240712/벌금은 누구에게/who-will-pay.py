n, m, k = list(map(int, input().split()))
student = [0 for i in range(n)]
find = -1
for _ in range(m):
    num = int(input())
    student[num - 1] += 1
    for i in range(n):
        if student[i] >= k:
            find = i + 1
            break
    if find != -1:
        break
print(find)