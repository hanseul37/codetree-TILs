arr = input().split()
a, b = int(arr[0]), int(arr[1])
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
ins = 0
for i in range(len(bb)):
    if bb[i] not in aa:
        ins = 2

gap = aa.index(bb[0])
for i in range(1, len(bb)):
    if aa[i + gap] != bb[i]:
        ins = 1

if ins != 0:
    print('No')
else:
    print('Yes')