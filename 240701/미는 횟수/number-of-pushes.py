A = input()
B = input()
n = 0
for i in range(len(A)):
    A = A[-1] + A[0:-1]
    n += 1
    if A == B:
        break
if n == len(A):
    print(-1)
else:
    print(n)