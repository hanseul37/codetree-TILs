n = int(input())
a = list(input())
b = list(input())
cnt = 0
for i in range(n - 1, -1, -1):
    if a[i] != b[i]:
        for j in range(i):
            if a[j] == 'G':
                a[j] = 'H'
            else:
                a[j] = 'G'
        cnt += 1
print(cnt) 

