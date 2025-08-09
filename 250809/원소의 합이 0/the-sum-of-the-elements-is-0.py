n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
ab = {}
cnt = 0
for x in a:
    for y in b:
        if x + y in ab:
            ab[x + y] += 1
        else:
            ab[x + y] = 1
for x in c:
    for y in d:
        if 0 - x - y in ab:
            cnt += ab[0 - x - y]

print(cnt)