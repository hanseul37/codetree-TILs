n = int(input())
a = input()
b = input()
cnt, prev = 0, 0
for i in range(n):
    if a[i] != b[i]:
        now = 1
    else:
        now = 0
    if now == 1 and prev == 0:
        cnt += 1
    prev = now
print(cnt)
    
