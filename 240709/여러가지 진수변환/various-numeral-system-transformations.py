N, B = list(map(int, input().split()))
arr = []
while N >= 2:
    arr.append(N % B)
    N //= B
if N != 0:
    arr.append(N)
for bit in arr[::-1]:
    print(bit, end='')