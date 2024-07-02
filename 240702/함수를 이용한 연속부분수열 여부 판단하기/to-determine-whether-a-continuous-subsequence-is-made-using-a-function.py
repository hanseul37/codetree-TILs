def check(A, B):
    for i in range(len(A) - len(B) + 1):
        if A[i:i+len(B)] == B:
            return True
    return False

a, b = list(map(int, input().split()))
A = input().split()
B = input().split()
if check(A, B):
    print('Yes')
else:
    print('No')